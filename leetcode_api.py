import json
from typing import Any

import requests


class LeetCodeApi:

    def __init__(self):
        self.session = requests.Session()
        self.session.get('https://leetcode.com/problemset/all/')
        self.session.headers['Referer'] = 'https://leetcode.com/problemset/all/'
        self.session.headers['X-csrftoken'] = self.session.cookies.get(
            'csrftoken')

    def send_graphql_post(
            self,
            endpoint: str,
            variables: dict[str, Any] | None = None) -> dict[str, Any]:
        payload = getattr(LeetCodeApiEndpoints, endpoint)
        payload['variables'] = variables
        response = self.session.post('https://leetcode.com/graphql/',
                                     json=payload)
        data = json.loads(response.text)

        if 'errors' in data:
            raise LeetCodeApiError(data['errors'])
        return data['data']

    def question_title(self, title_slug: str) -> dict[str, Any]:
        data = self.send_graphql_post('questionTitle',
                                      {'titleSlug': title_slug})
        if data['question'] is None:
            raise LeetCodeApiError(f'Question not found: {title_slug}')
        return data['question']

    def default_code(self,
                     title_slug: str,
                     lang_slug: str | None = 'cpp') -> str:
        data = self.send_graphql_post('questionEditorData',
                                      {'titleSlug': title_slug})
        for snippet in data['question']['codeSnippets']:
            if snippet['langSlug'] == lang_slug:
                return snippet['code']
        raise LeetCodeApiError(
            f'Default code not found for language: {lang_slug}')


class LeetCodeApiEndpoints:

    # yapf: disable
    questionOfTheDay = {
        'query': '\n    query questionOfToday {\n  activeDailyCodingChallengeQuestion {\n    date\n    userStatus\n    link\n    question {\n      acRate\n      difficulty\n      freqBar\n      frontendQuestionId: questionFrontendId\n      isFavor\n      paidOnly: isPaidOnly\n      status\n      title\n      titleSlug\n      hasVideoSolution\n      hasSolution\n      topicTags {\n        name\n        id\n        slug\n      }\n    }\n  }\n}\n    ',
        'variables': {},
        'operationName': 'questionOfToday'
    }
    questionTitle = {
        'query': '\n    query questionTitle($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    title\n    titleSlug\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n  }\n}\n    ',
        'variables': {
            'titleSlug': 'TITLE_SLUG'
        },
        'operationName': 'questionTitle'
    }
    questionEditorData = {
        'query': '\n    query questionEditorData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    codeSnippets {\n      lang\n      langSlug\n      code\n    }\n    envInfo\n    enableRunCode\n  }\n}\n    ',
        'variables': {
            'titleSlug': 'TITLE_SLUG'
        },
        'operationName': 'questionEditorData'
    }
    questionContent = {
        'query': '\n    query questionContent($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    content\n    mysqlSchemas\n  }\n}\n    ',
        'variables': {
            'titleSlug': 'TITLE_SLUG'
        },
        'operationName': 'questionContent'
    }
    consolePanelConfig = {
        'query': '\n    query consolePanelConfig($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    questionTitle\n    enableDebugger\n    enableRunCode\n    enableSubmit\n    enableTestMode\n    exampleTestcaseList\n    metaData\n  }\n}\n    ',
        'variables': {
            'titleSlug': 'TITLE_SLUG'
        },
        'operationName': 'consolePanelConfig'
    }
    # yapf: enable


class LeetCodeApiError(Exception):
    pass
