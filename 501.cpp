// Ref: https://leetcode.com/problems/find-mode-in-binary-search-tree/solutions/98191/c-o-n-time-and-o-1-space-by-inorder-traversal

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
    int max_freq = 0, cur_freq = 0, pre = -100001;
    vector<int> ans;

    vector<int> findMode(TreeNode* root) {
        dfs(root);
        return ans;
    }

    void dfs(TreeNode *node) {
        if (node == nullptr) {
            return;
        }

        dfs(node->left);
        if (pre == node->val) {
            cur_freq++;
        } else {
            cur_freq = 1;
        }
        if (cur_freq > max_freq) {
            ans.clear();
            max_freq = cur_freq;
            ans.push_back(node->val);
        } else if (cur_freq == max_freq) {
            ans.push_back(node->val);
        }
        pre = node->val;
        dfs(node->right);
    }
};

