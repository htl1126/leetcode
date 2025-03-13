// ref: https://leetcode.com/problems/partition-array-for-maximum-sum/solutions/290863/java-c-python-dp-o-k-space/

class Solution {
public:
    int maxSumAfterPartitioning(vector<int>& arr, int K) {
        int n = arr.size();
        vector<int> dp(K);
        for (int i = 1; i <= n; i++) {
            int curMax = 0, best = 0;
            for (int k = 1; k <= K && i - k >= 0; k++) {
                curMax = max(curMax, arr[i - k]);
                best = max(best, dp[(i - k) % K] + curMax * k);
            }
            dp[i % K] = best;
        }

        return dp[n % K];
    }
};

