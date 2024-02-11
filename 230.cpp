// Ref: https://leetcode.com/problems/toss-strange-coins/solutions/408485/java-c-python-dp

class Solution {
public:
    double probabilityOfHeads(vector<double>& prob, int target) {
        vector<double> dp(target + 1);
        dp[0] = 1.0;  // dp[0] here refers to dp[0][0]
        for (int i = 0; i < prob.size(); i++) {
            for (int k = min(i + 1, target); k >= 0; k--) {
                // The dp[i] in the previous iteration dp[c][i] becomes dp[c - 1][i]
                // in the current iteration, so we do the calculation backwards.
                if (k > 0) {
                    dp[k] = dp[k - 1] * prob[i] + dp[k] * (1 - prob[i]);
                } else {
                    dp[k] = dp[k] * (1 - prob[i]);
                }
            }
        }
        return dp[target];
    }
};

