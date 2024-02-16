# LeetCode helper

Helper scripts and files to speed up my workflow of solving LeetCode daily.

- **`fetch.py`:** Main script that fetches a given LeetCode problem and creates a solution source file with default code of the problem. If title slug is not provided, it fetches the active problem of Daily LeetCoding Challenge. For more information, refer to the script's help message.
- **`leetcode_api.py`**: Library to send requests to LeetCode's GraphQL API. It only includes endpoints that are used in this project. Note that LeetCode has no offical documentation for its GraphQL API, so the endpoints are extracted from browser network traffic.
- **`main_template.cpp`**: Template code for the main program. It contains macros and functions for debugging, as well as code that drives the `Solution` class.
- **`leetcode_util.h`**: Definition of LeetCode's `ListNode` and `TreeNode` data types, and helper functions to construct and print them.
