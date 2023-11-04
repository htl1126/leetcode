// Ref: https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/solutions/1238655/java-c-python-min-max
class Solution {
public:
    int minPairSum(vector<int>& nums) {
        int ans = 0, n = nums.size();
        sort(nums.begin(), nums.end());
        for (int i = 0; i < n / 2; i++) {
            ans = max(ans, nums.at(i) + nums.at(n - i - 1));
        }
        return ans;
    }
};

