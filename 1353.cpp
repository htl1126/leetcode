// Ref: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/discuss/510263/JavaC%2B%2BPython-Priority-Queue

class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        priority_queue <int, vector<int>, greater<int>> pq;
        sort(events.begin(), events.end());
        int i = 0, ans = 0, d = 0, n = events.size();
        while (pq.size() > 0 || i < n) {
            if (pq.size() == 0) {
                d = events[i][0];
            }
            while (i < n && events[i][0] == d) {
                pq.push(events[i++][1]);
            }
            pq.pop();
            ans++, d++;
            while (pq.size() > 0 && pq.top() < d) {
                pq.pop();
            }
        }
        return ans;
    }
};
