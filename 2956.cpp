class Solution {
public:
    vector<int> findIntersectionValues(vector<int>& nums1, vector<int>& nums2) {
        set<int> set1(nums1.begin(), nums1.end());
        set<int> set2(nums2.begin(), nums2.end());
        int res1 = 0, res2 = 0;

        for (const auto& n : nums1) {
            if (set2.count(n) > 0) {
                res1++;
            }
        }
        for (const auto& n : nums2) {
            if (set1.count(n) > 0) {
                res2++;
            }
        }

        return {res1, res2};
    }
};

