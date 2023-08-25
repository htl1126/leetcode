// Ref: https://leetcode.com/problems/sort-array-by-parity-ii/solutions/181158/c-5-lines-two-pointers-2-liner-bonus/

class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& nums) {
        for (int i = 0, j = 1; i < nums.size(); i += 2, j += 2) {
            while (i < nums.size() && nums[i] % 2 == 0) {
                i += 2;
            }
            while (j < nums.size() && nums[j] % 2 == 1) {
                j += 2;
            }
            // Since nums has equal number of even and odd values,
            // when we have i < nums.size() which means all the values
            // at even indexes are even AND all the values at odd indexes
            // are odd, we don't have to check if j < nums.size().
            if (i < nums.size()) {
                swap(nums[i], nums[j]);
            }
        }
        return nums;
    }
};
