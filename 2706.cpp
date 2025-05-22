class Solution {
public:
    int buyChoco(vector<int>& prices, int money) {
        int first = min(prices[0], prices[1]), second = max(prices[0], prices[1]);

        for (int i = 2; i < prices.size(); i++) {
            if (first < prices[i] && prices[i] < second) {
                second = prices[i];
            } else if (prices[i] <= first) {
                second = first;
                first = prices[i];
            }
        }
        if (first + second > money) {
            return money;
        }
        return money - first - second;
    }
};

