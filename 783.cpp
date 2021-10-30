// ref: https://leetcode.com/problems/minimum-distance-between-bst-nodes/discuss/114834/C%2B%2BJavaPython-Inorder-Traversal-O(N)-time-Recursion

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int pre{-1}, res{INT_MAX};
    int minDiffInBST(TreeNode* root) {
        if (root->left) {
            minDiffInBST(root->left);
        }
        if (pre >= 0) {
            res = min(res, root->val - pre);
        }
        pre = root->val;
        if (root->right) {
            minDiffInBST(root->right);
        }
        return res;
    }
};
