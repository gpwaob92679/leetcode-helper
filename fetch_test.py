import pathlib
import subprocess
import sys
import unittest

_SCRIPT = (pathlib.Path(__file__).parent / 'fetch.py').resolve()
_SOLUTION_DIR = (pathlib.Path(__file__).parent / 'temp').resolve()


class FetchTest(unittest.TestCase):

    def setUp(self):
        if _SOLUTION_DIR.exists():
            for p in _SOLUTION_DIR.iterdir():
                p.unlink()

    def test_daily(self):
        subprocess.run([sys.executable, _SCRIPT, '-d', _SOLUTION_DIR],
                       check=True)
        # Check if the solution file placeholder in main.cpp is correctly
        # replaced.
        with open(_SOLUTION_DIR / 'main.cpp', 'r', encoding='utf-8') as f:
            self.assertRegex(f.read(), r'#include "\d+\. .+\.cpp"')

    def test_slug(self):
        subprocess.run(
            [sys.executable, _SCRIPT, '-d', _SOLUTION_DIR, 'two-sum'],
            check=True)
        with open(_SOLUTION_DIR / '1. Two Sum.cpp', 'r', encoding='utf-8') as f:
            expected = (
                'class Solution {\n'
                'public:\n'
                '    vector<int> twoSum(vector<int>& nums, int target) {\n'
                '        \n'
                '    }\n'
                '};')
            self.assertMultiLineEqual(f.read(), expected)
        with open(_SOLUTION_DIR / 'main.cpp', 'r', encoding='utf-8') as f:
            self.assertIn('#include "1. Two Sum.cpp"', f.read())


if __name__ == '__main__':
    unittest.main()
