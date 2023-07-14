// Ref: https://leetcode.com/problems/time-needed-to-buy-tickets/solutions/1576932/c-one-pass/

class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        int ans = 0;
        for (int i = 0; i < tickets.size(); i++) {
            ans += min(tickets[k] - (i > k), tickets[i]);
        }
        return ans;
    }
};
