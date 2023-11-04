class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int r = strs.size(), c = strs.at(0).size();
        int ans = 0;
        for (int j = 0; j < c; j++) {
            for (int i = 0; i < r - 1; i++) {
                if (strs.at(i).at(j) > strs.at(i + 1).at(j)) {
                    ans++;
                    break;
                }
            }
        }

        return ans;
    }
};

