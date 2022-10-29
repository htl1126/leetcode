// Ref: https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/discuss/2168227/JavaC%2B%2BPython-One-Pass-O(n)

class Solution {
public:
    int longestSubsequence(string s, int k) {
        int ans = 0, cost = 1, n = s.size();
        for (int i = n - 1; i >= 0; i--) {
            if (s.at(i) == '0' || cost <= k) {
                k -= cost * (s.at(i) - '0');
                ans++;
            }
            if (cost <= k) {
                cost *= 2;
            }
        }
        return ans;
    }
};
