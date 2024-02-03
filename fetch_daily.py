from pathlib import Path
import shutil
import sys

import leetcode_api


def prompt():
    choice = input('Proceed? [y/N]')
    if choice not in ('Y', 'y', 'yes'):
        print('Abort')
        sys.exit(1)


def main():
    api = leetcode_api.LeetCodeApi()
    daily_slug = api.send_graphql_post('questionOfTheDay')[
        'activeDailyCodingChallengeQuestion']['question']['titleSlug']
    print(f'{daily_slug = }')

    # Generate solution cpp file
    solution_cpp = Path('../'
                        f'{api.question_id(daily_slug)}. '
                        f'{api.question_title(daily_slug)}.cpp')
    print(f'{solution_cpp = }')
    if solution_cpp.exists():
        print(f'Solution file already exists: {solution_cpp.name}')
        prompt()
    with open(solution_cpp, 'w', encoding='utf-8') as f:
        f.write(api.default_code(daily_slug))

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
