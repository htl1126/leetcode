class Solution {
public:
    int arraySign(vector<int>& nums) {
        int neg_cnt = 0;

        for (const auto& n : nums) {
            if (n < 0) {
                neg_cnt += 1;
            } else if (n == 0) {
                return 0;
            }
        }

        return neg_cnt & 1 ? -1 : 1;
    }
};

