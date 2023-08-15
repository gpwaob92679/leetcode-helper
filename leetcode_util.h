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
}  // namespace leetcode_util

#endif  // LEETCODE_UTIL_H_
