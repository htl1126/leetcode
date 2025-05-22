// https://leetcode.com/problems/rearrange-array-elements-by-sign/solutions/1711413/c-two-pointer-o-n

class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        vector<int> ans(nums.size());

        int pos_i = 0, neg_i = 1;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > 0) {
                ans[pos_i] = nums[i];
                pos_i += 2;
            } else {
                ans[neg_i] = nums[i];
                neg_i += 2;
            }
        }

        return ans;
    }
};

