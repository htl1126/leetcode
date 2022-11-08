// Ref: https://leetcode.com/problems/merge-in-between-linked-lists/discuss/952044/C%2B%2B-easy-approch

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode *start = list1, *end = list1;
        for (int i = 0; i < b; i++) {
            if (i < a - 1) {
                start = start->next;
            }
            end = end->next;
        }
        start->next = list2;
        while (list2->next != nullptr) {
            list2 = list2->next;
        }
        list2->next = end->next;
        return list1;
    }
};
