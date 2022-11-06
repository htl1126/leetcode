// Ref: https://leetcode.com/problems/two-sum/discuss/13/Accepted-C%2B%2B-O(n)-Solution

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n;
        unordered_map<int, int> d;
        vector<int> ans;
        for (int i = 0; i < nums.size(); i++) {
            n = target - nums[i];
            if (d.find(n) != d.end()) {
                ans.push_back(d[n]);
                ans.push_back(i);
                return ans;
            }
            d[nums[i]] = i;
        }
        return ans;
    }
};
