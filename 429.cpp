// Ref: https://leetcode.com/problems/n-ary-tree-level-order-traversal/solutions/1386593/c-python-bfs-dfs-solutions-clean-concise

/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        if (root == nullptr) {
            return {};
        }
        queue<Node *> q;
        q.push(root);
        vector<vector<int>> ans;
        while (!q.empty()) {
            ans.push_back({});
            for (int i = q.size() - 1; i >= 0; i--) {  // should not put "i < q.size() - 1" as the condition since q.size() is not a constant
                Node *cur = q.front();
                q.pop();
                ans.back().push_back(cur->val);
                for (auto child : cur->children) {
                    q.push(child);
                }
            }
        }
        return ans;
    }
};

