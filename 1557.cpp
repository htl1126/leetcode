// Ref: https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/solutions/805685/java-c-python-nodes-with-no-in-degree/
class Solution {
public:
    vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
        vector<int> ans, seen(n);
        for (auto const&e : edges) {
            seen[e[1]] = 1;
        }
        for (int i = 0; i < n; i++) {
            if (seen[i] == 0) {
                ans.push_back(i);
            }
        }
        return ans;
    }
};

