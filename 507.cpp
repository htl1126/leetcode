class Solution {
public:
    bool checkPerfectNumber(int num) {
        if (num == 1) {
            return false;
        }

        int n = 2, ans = 1;
        for (; n < sqrt(num); n++) {
            if (num % n == 0) {
                ans += n + num / n;
            }
        }

        if (n * n == num) {
            ans += n;
        }

        return ans == num;
    }
};
