// Ref: https://leetcode.com/problems/last-stone-weight-ii/solutions/294888/java-c-python-easy-knapsacks-dp/

class Solution {
public:
    int lastStoneWeightII(vector<int>& stones) {
        bitset<1501> dp;
        dp.set(0, true);
        int total = 0;
        for (const auto& stone : stones) {
            total += stone;
            for (int i = min(1500, total); i >= stone; --i) {
                dp[i] = dp[i] | dp[i - stone];
            }
        }
        for (int i = total / 2; i >= 0; --i) {
            if (dp[i]) {
                return (total - i) - i;
            }
        }
        return 0;
    }
};

