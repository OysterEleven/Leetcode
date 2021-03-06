#include "stdafx.h";
#include<vector>;
using namespace std;

struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
	ListNode * mergeKLists(vector<ListNode*>& lists) {
		if (lists.empty())
			return nullptr;
		return helper(lists, 0, lists.size() - 1);
	}

	ListNode* helper(vector<ListNode*>& Lists, int left, int right)
	{
		if (left == right)
			return Lists[left];
		if (left < right) {
			int mid = (left + right) / 2;
			ListNode *l1 = helper(Lists, left, mid);
			ListNode *l2 = helper(Lists, mid + 1, right);
			return merge2Lists(l1, l2);
		}
		return nullptr;
	}

	ListNode* merge2Lists(ListNode *l1, ListNode *l2)
	{
		if (l1 == nullptr)
			return l2;
		if (l2 == nullptr)
			return l1;
		if (l1->val <= l2->val) {
			l1->next = merge2Lists(l1->next, l2);
			return l1;
		}
		else {
			l2->next = merge2Lists(l1, l2->next);
			return l2;
		}
	}
};
