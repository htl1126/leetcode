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
    int count = 0;
    pair<int, int> dfs(TreeNode* node) { // return {sum_of_val, sum_of_node_count}
        if (node == nullptr) {
            return {0, 0};
        }

        auto left = dfs(node->left), right = dfs(node->right);
        int sum_of_val = left.first + node->val + right.first;
        int sum_of_node_count = left.second + 1 + right.second;
        if (sum_of_val / sum_of_node_count == node->val) {
            count++;
        }

        return {sum_of_val, sum_of_node_count};
    }

    int averageOfSubtree(TreeNode* root) {
        dfs(root);
        return count;
    }
};

