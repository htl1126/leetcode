// Ref: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/submissions

class Solution {
public:
    int findTheCity(int n, vector<vector<int>>& edges, int distanceThreshold) {
        int ans = 0, smallest = n;
        vector<vector<int>> dis(n, vector<int>(n, 10001));
        for (int i = 0; i < n; i++) {
            dis[i][i] = 0;
        }
        for (auto const& e : edges) {
            dis[e[0]][e[1]] = dis[e[1]][e[0]] = e[2];
        }
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]);
                }
            }
        }
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++) {
                if (dis[i][j] <= distanceThreshold) {
                    count++;
                }
            }
            if (count <= smallest) {
                smallest = count;
                ans = i;
            }
        }
        return ans;
    }
};

