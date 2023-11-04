// Ref: https://leetcode.com/problems/longest-nice-substring/solutions/1074856/c-o-n

class Solution {
public:
    string longestNiceSubstring(string s, int start = 0, int end = -1) {
        if (end == -1) {
            end = s.size();
        }
        vector<vector<int>> count(26, vector<int>(2, 0));
        int j = start - 1;
        for (int i = start; i < end; i++) {
            count.at(tolower(s.at(i)) - 'a').at((bool)islower(s.at(i))) = 1;
        }
        string ans;
        for (int i = start; i <= end; i++) {
            int ch = (i == end ? -1 : tolower(s.at(i)) - 'a');
            if (i == end || count.at(ch).at(0) + count.at(ch).at(1) == 1) {
                // until the end we don't see any alphabet appearing for only once
                if (j == -1 && i == end) {
                    return s;
                }
                // s.at(i) is the "single" char, and we recursively
                // find the answer for s[j, i - 1]
                string new_ans = longestNiceSubstring(s.substr(j + 1, i - (j + 1)));
                if (new_ans.size() > ans.size()) {
                    ans = new_ans;
                }
                // search from s[i + 1, s.size() - 1] for the next iteration
                j = i;
            }
        }
        return ans;
    }
};

