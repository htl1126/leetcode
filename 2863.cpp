// ref: https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/solutions/4070047/linear-time-solution-in-c-java-python/
class Solution {
public:
    int maxSubarrayLength(vector<int>& nums) {
        stack<int> stack;
        int n = nums.size();

        for (int i = n - 1; i >= 0; i--) {
            if (stack.empty() || nums[i] < nums[stack.top()]) {
                stack.push(i);
            }
        }

        int ans = 0;
        for (int i = 0, curMax = INT_MIN; !stack.empty() && i < n; i++) {
            while (!stack.empty() && i >= stack.top()) {
                stack.pop();
            }

            if (nums[i] > curMax) {
                curMax = nums[i];
                while (!stack.empty() && nums[i] > nums[stack.top()]) {
                    ans = max(ans, stack.top() - i + 1);
                    stack.pop();
                }
            }
        }
        return ans;
    }
};

