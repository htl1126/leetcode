// Ref: https://leetcode.com/problems/fair-distribution-of-cookies/solutions/2141573/dp-submask-enumeration-most-optimal-solution-100-faster-c

class Solution {
public:
    int distributeCookies(vector<int>& cookies, int k) {
        int n = cookies.size();
        vector<vector<int>> dp(k + 1, vector<int>(1LL << n, INT_MAX));

        vector<int> sum(1LL << n);
        for (int mask = 0; mask < (1LL << n); mask++) {
            int total = 0;
            for (int i = 0; i < n; i++) {
                //cout << (mask & (1LL << i)) << endl;
                if (mask & (1LL << i)) {
                    total += cookies[i];
                }
            }
            sum[mask] = total;
        }

        dp[0][0] = 0;
        for (int person = 1; person <= k; person++) {
            for (int mask = 0; mask < (1LL << n); mask++) {
                // iterate over all the submasks
                for (int submask = mask; submask; submask = (submask - 1) & mask) {
                    // sum[submask]: sum of cookies[i] where ith bit of submask is 1
                    // given submask, submask + (submask ^ mask) = mask
                    dp[person][mask] = min(dp[person][mask], max(sum[submask], dp[person - 1][submask ^ mask]));
                }
            }
        }
        return dp[k][(1LL << n) - 1];
    }
};

