// Ref: https://leetcode.com/problems/path-with-maximum-probability/solutions/3691291/c-code-with-comments-dijkstra-algorithm

class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        vector<vector<pair<int, double>>> adj(n);
        for (int i = 0; i < edges.size(); i++) {
            adj[edges[i][0]].push_back({edges[i][1], succProb[i]});
            adj[edges[i][1]].push_back({edges[i][0], succProb[i]});
        }

        priority_queue<pair<double, int>> pq;
        pq.push({1.0, start_node});
        vector<double> dist(n, -1);
        dist[start_node] = 1;

        while (!pq.empty()) {
            auto [dis, cur_v] = pq.top();
            pq.pop();
            for (auto& [v, w] : adj[cur_v]) {
                if (dist[v] < dis * w) {
                    dist[v] = dis * w;
                    pq.push({dist[v], v});
                }
            }
        }

        if (dist[end_node] < 0) {
            return 0.0;
        } else {
            return dist[end_node];
        }
    }
};

