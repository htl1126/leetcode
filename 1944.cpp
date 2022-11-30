// Ref: https://leetcode.com/problems/number-of-visible-people-in-a-queue/discuss/1359707/JavaC%2B%2BPython-Stack-Solution-Next-Greater-Element

class Solution {
public:
    vector<int> canSeePersonsCount(vector<int>& heights) {
        int n = heights.size();
        vector<int> ans(n), stack;
        for (int i = 0; i < n; i++) {
            while (!stack.empty() && heights[stack.back()] <= heights[i]) {
                ans[stack.back()]++;
                stack.pop_back();
            }
            if (!stack.empty()) {
                ans[stack.back()]++;
            }
            stack.push_back(i);
        }
        return ans;
    }
};
