// Ref: https://leetcode.com/problems/rank-teams-by-votes/solutions/524869/c-python-count-votes/

class Solution {
public:
    string rankTeams(vector<string>& votes) {
        string ans;
        vector<vector<int>> count(26, vector<int>(27));
        for (char& c : votes.at(0)) {
            count.at(c - 'A').at(26) = c;
        }
        for (const string& vote : votes) {
            for (int i = 0; i < vote.size(); i++) {
                count.at(vote.at(i) - 'A').at(i)--;
            }
        }
        sort(count.begin(), count.end());
        for (int i = 0; i < votes.at(0).size(); i++) {
            ans += count.at(i).at(26);
        }
        return ans;
    }
};

