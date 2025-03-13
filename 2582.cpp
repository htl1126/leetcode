// ref: https://leetcode.com/problems/pass-the-pillow/solutions/3258156/java-c-python-one-line-o-1/

class Solution {
public:
    int passThePillow(int n, int time) {
        return n - abs(n - 1 - time % (n * 2 - 2));
    }
};

