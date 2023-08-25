// Ref: https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/solutions/1407800/c-c-java-js-python-1-liner-simple-and-short-solutions-faster-than-100

class Solution {
public:
    bool areOccurrencesEqual(string s) {
        unordered_map<char, int> freq;
        for (auto c : s) {
            freq[c]++;
        }
        int v = freq[s[0]];
        for (auto [c, f] : freq) {
            if (f != v) {
                return false;
            }
        }
        return true;
    }
};
