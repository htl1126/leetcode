// Ref: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/solutions/465585/java-c-python-find-the-rule/

class Solution {
public:
    vector<int> sumZero(int n) {
        vector<int> ans(n);
        for (int i = 0; i < n; i++) {
            ans[i] = i * 2 - n + 1;
        }
        return ans;
    }
};
