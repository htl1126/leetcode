// Ref: https://leetcode.com/problems/frequency-of-the-most-frequent-element/discuss/1175090/JavaC%2B%2BPython-Sliding-Window

class Solution {
public:
    int maxFrequency(vector<int>& nums, long k) {
        int i = 0, j;
        sort(nums.begin(), nums.end());
        for (j = 0; j < nums.size(); j++) {
            k += nums[j];
            if (k < (long)nums[j] * (j - i + 1)) {
                k -= nums[i++];
            }
        }
        return j - i;
    }
};
