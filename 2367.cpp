// ref: https://leetcode.com/problems/number-of-arithmetic-triplets/solutions/2390637/check-n-diff-and-n-2-diff

class Solution {
public:
    int arithmeticTriplets(vector<int>& nums, int diff) {
        int res = 0;
        vector<int> table(201, 0);

        for (const auto& n : nums) {
            if (n >= 2 * diff && table[n - diff] && table[n - 2 * diff]) {
                res++;
            }
            table[n] = 1;
        }

        return res;
    }
};

