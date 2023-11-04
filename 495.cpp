class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        int ans = 0, n = timeSeries.size();
        timeSeries.push_back(10000001);
        for (int i = 0; i < n; i++) {
            if (timeSeries.at(i) + duration - 1 < timeSeries.at(i + 1)) {
                ans += duration;
            } else {
                ans += timeSeries.at(i + 1) - timeSeries.at(i);
            }
        }
        return ans;
    }
};

