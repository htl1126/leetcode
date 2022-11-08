// Ref: https://leetcode.com/problems/find-the-difference-of-two-arrays/discuss/1886953/set_difference

class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        vector<int> ans0, ans1;
        set<int> s1(begin(nums1), end(nums1)), s2(begin(nums2), end(nums2));
        set_difference(s1.begin(), s1.end(), s2.begin(), s2.end(), back_inserter(ans0));
        set_difference(s2.begin(), s2.end(), s1.begin(), s1.end(), back_inserter(ans1));
        return {ans0, ans1};
    }
};
