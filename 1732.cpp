class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int cur = 0, res = 0;

        for (const auto& diff : gain) {
            cur += diff;
            res = max(res, cur);
        }

        return res;
    }
};

