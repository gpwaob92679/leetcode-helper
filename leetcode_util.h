#ifndef LEETCODE_UTIL_H_
#define LEETCODE_UTIL_H_

namespace leetcode_util {
#pragma GCC diagnostic ignored "-Wshadow"
struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};
#pragma GCC diagnostic pop

ListNode *BuildList(const size_t size) {
  vector<ListNode *> nodes(size);
  nodes[0] = new ListNode(1);
  for (size_t i = 1; i < size; ++i) {
    nodes[i] = new ListNode(i + 1);
    nodes[i - 1]->next = nodes[i];
  }
  return nodes[0];
}
ListNode *BuildList(const vector<int> &nums) {
  vector<ListNode *> nodes(nums.size());
  nodes[0] = new ListNode(nums[0]);
  for (size_t i = 1; i < nums.size(); ++i) {
    nodes[i] = new ListNode(nums[i]);
    nodes[i - 1]->next = nodes[i];
  }
  return nodes[0];
}

void PrintList(ListNode *head) {
  cerr << '{';
  for (ListNode *node = head; node; node = node->next) {
    cerr << node->val << (node->next ? " -> " : "");
  }
  cerr << '}' << endl;
}

TreeNode *BuildTree(const size_t index, const vector<int> &nums) {
  TreeNode *node = new TreeNode(nums[index]);
  if (index * 2 + 1 < nums.size() && nums[index * 2 + 1] != -1) {
    node->left = BuildTree(index * 2 + 1, nums);
  }
  if (index * 2 + 2 < nums.size() && nums[index * 2 + 2] != -1) {
    node->right = BuildTree(index * 2 + 2, nums);
  }
  return node;
}

void PrintTree(const TreeNode *node) {
  if (node->left) {
    PrintTree(node->left);
  }
  cerr << node->val << ' ';
  if (node->right) {
    PrintTree(node->right);
  }
}
}  // namespace leetcode_util

#endif  // LEETCODE_UTIL_H_
