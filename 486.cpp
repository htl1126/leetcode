// Ref: https://leetcode.com/problems/predict-the-winner/solutions/96828/java-9-lines-dp-solution-easy-to-understand-with-improvement-to-o-n-space-complexity/

class Solution {
public:
    bool predictTheWinner(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(nums.size());
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (i == j) {
                    dp[j] = nums[j];
                } else {
                    // first dp[j] == dp[i][j] for the 2D solution
                    // second dp[j] == dp[i + 1][j] for the 2D solution
                    // on the right, dp[j - 1] == dp[i][j - 1] for the 2D solution
                    dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1]);
                }
            }
        }
        return dp[n - 1] >= 0;
    }
};

