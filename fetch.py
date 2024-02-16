import argparse
from pathlib import Path
import shutil
import sys

import leetcode_api

parser = argparse.ArgumentParser()
parser.add_argument(
    'slug',
    nargs='?',
    help='Title slug of the problem. If not provided, fetch the daily problem.')
args = parser.parse_args()


def prompt():
    choice = input('Proceed? [y/N]')
    if choice not in ('Y', 'y', 'yes'):
        print('Abort')
        sys.exit(1)


def main():
    api = leetcode_api.LeetCodeApi()
    slug = args.slug or (
        api.send_graphql_post('questionOfTheDay')
        ['activeDailyCodingChallengeQuestion']['question']['titleSlug'])
    print(f'{slug = }')
    question_title = api.question_title(slug)

    # Generate solution cpp file
    solution_cpp = Path('../'
                        f'{question_title["questionFrontendId"]}. '
                        f'{question_title["title"]}.cpp')
    print(f'{solution_cpp = }')
    if solution_cpp.exists():
        print(f'Solution file already exists: {solution_cpp.name}')
        prompt()
    with open(solution_cpp, 'w', encoding='utf-8') as f:
        f.write(api.default_code(slug))

    # Generate main.cpp
    main_cpp = Path('../main.cpp')
    if main_cpp.exists():
        shutil.copy2(main_cpp, '../main_old.cpp')
    shutil.copyfile('main_template.cpp', main_cpp)

    # TODO: Auto generate input variables and test cases
    with open(main_cpp, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].replace('@SOLUTION_SOURCE@', solution_cpp.name)
        f.seek(0)
        f.writelines(lines)


if __name__ == '__main__':
    main()
