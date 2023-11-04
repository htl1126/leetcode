// Ref: https://leetcode.com/problems/substrings-that-begin-and-end-with-the-same-letter/solutions/1603481/n-th-char-adds-n-substrings

class Solution {
public:
    long long numberOfSubstrings(string s) {
        long long ans = 0LL;
        vector<long long> count(26);
        for (const auto& c : s) {
            count.at(c - 'a')++;
        }
        for (const auto& v : count) {
            ans += v * (v + 1) / 2;
        }
        return ans;
    }
};

