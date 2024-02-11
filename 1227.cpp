// Ref: https://medium.com/i-math/solving-an-advanced-probability-problem-with-virtually-no-math-5750707885f1

class Solution {
public:
    double nthPersonGetsNthSeat(int n) {
        if (n == 1) {
            return 1.0;
        }
        return 0.5;
    }
};

