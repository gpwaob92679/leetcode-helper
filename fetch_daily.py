import json
from typing import Any
from pathlib import Path
import shutil

import requests


def write_to_file(path, obj) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(obj)


class ApiError(Exception):
    pass


class LeetCodeApi:

    def __init__(self):
        self.session = requests.Session()
        self.session.get("https://leetcode.com/problemset/all/")
        self.headers = {
            "Referer": "https://leetcode.com/problemset/javascript/",
            "X-csrftoken": self.session.cookies.get("csrftoken"),
        }

        with open("endpoints.json", 'r', encoding="utf-8") as f:
            self.endpoints = json.load(f)

    def send_graphql_post(
            self,
            endpoint: str,
            variables: dict[str, Any] | None = None) -> dict[str, Any]:
        payload = self.endpoints[endpoint]
        payload["variables"] = variables
        response = self.session.post("https://leetcode.com/graphql/",
                                     json=payload,
                                     headers=self.headers)
        data = json.loads(response.text)

        if "errors" in data:
            raise ApiError(data["errors"])
        return data["data"]

    def question_title(self, title_slug: str) -> str:
        data = self.send_graphql_post("questionTitle",
                                      {"titleSlug": title_slug})
        return data["question"]["title"]

    def question_id(self, title_slug: str) -> str:
        data = self.send_graphql_post("questionTitle",
                                      {"titleSlug": title_slug})
        return data["question"]["questionFrontendId"]

    def default_code(self,
                     title_slug: str,
                     lang_slug: str | None = "cpp") -> str:
        data = self.send_graphql_post("questionEditorData",
                                      {"titleSlug": title_slug})
        snippet = next(x for x in data["question"]["codeSnippets"]
                       if x["langSlug"] == lang_slug)
        return snippet["code"]


def main():
    api = LeetCodeApi()
    daily_slug = api.send_graphql_post("questionOfTheDay")[
        "activeDailyCodingChallengeQuestion"]["question"]['titleSlug']
    print(f"{daily_slug = }")

    # Generate solution cpp file
    solution_cpp = Path("../"
                        f"{api.question_id(daily_slug)}. "
                        f"{api.question_title(daily_slug)}.cpp")
    if solution_cpp.exists():
        raise FileExistsError(f"Solution file \"{solution_cpp.name}\" already "
                              "exists.")
    with open(solution_cpp, "w", encoding="utf-8") as f:
        f.write(api.default_code(daily_slug))

    # Generate main.cpp
    main_cpp = Path("../main.cpp")
    if main_cpp.exists():
        shutil.copy2(main_cpp, "../main_old.cpp")
    shutil.copyfile("main_template.cpp", main_cpp)

    # TODO: Auto generate input variables and test cases
    with open(main_cpp, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].replace("@SOLUTION_SOURCE@", solution_cpp.name)
        f.seek(0)
        f.writelines(lines)


if __name__ == '__main__':
    main()
