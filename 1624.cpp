// Ref: https://leetcode.com/problems/largest-substring-between-two-equal-characters/solutions/899779/c-minimalizm/

class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        int ans = -1;
        vector<int> first_pos(26); // first occurrence for each alphabet

        for (int i = 0; i < s.size(); i++) {
            if (first_pos.at(s.at(i) - 'a') == 0) {
                first_pos.at(s.at(i) - 'a') = i + 1;
            }
            ans = max(ans, i - first_pos.at(s.at(i) - 'a'));
        }
        return ans;
    }
};

