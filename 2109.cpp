class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        string ans;
        int s_len = s.size(), spaces_len = spaces.size();
        ans.reserve(s_len + spaces_len);
        for (int i = 0, j = 0; i < s_len; i++) {
            if (j < spaces_len && i == spaces[j]) {
                ans += " ";
                j++;
            }
            ans += s[i];
        }
        return ans;
    }
};
