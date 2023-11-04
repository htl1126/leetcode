// Ref: https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/submissions

class Solution {
public:
    string evaluate(string s, vector<vector<string>>& knowledge) {
        int n = s.size();
        string ans = "";
        unordered_map<string, string> map;
        for (auto& pair : knowledge) {
            map[pair.at(0)] = pair.at(1);
        }
        for (int i = 0; i < n; i++) {
            if (s.at(i) == '(') {
                string key = "";
                for (i++; s.at(i) != ')'; i++) {
                    key += s.at(i);
                }
                ans += map.count(key) ? map[key] : "?";
            } else {
                ans += s.at(i);
            }
        }
        return ans;
    }
};

