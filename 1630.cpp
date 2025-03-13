// ref: https://leetcode.com/problems/arithmetic-subarrays/solutions/910421/c-two-approaches-140-vs-28ms/

class Solution {
public:
    vector<bool> checkArithmeticSubarrays(vector<int>& nums, vector<int>& l, vector<int>& r) {
        vector<bool> res;
        for (int i = 0, j = 0; i < l.size(); i++) {
            auto minMax = minmax_element(nums.begin() + l[i], nums.begin() + r[i] + 1);
            auto minV = minMax.first, maxV = minMax.second;
            int len = r[i] - l[i] + 1, d = (*maxV - *minV) / (len - 1);
            if (*minV == *maxV) {
                res.push_back(true);
            } else if ((*maxV - *minV) % (len - 1)) {
                res.push_back(false);
            } else {
                vector<bool> seen(len);
                for (j = l[i]; j <= r[i]; j++) {
                    if ((nums[j] - *minV) % d || seen[(nums[j] - *minV) / d]) {
                        break;
                    }
                    seen[(nums[j] - *minV) / d] = true;
                }
               
                res.push_back(j > r[i]);
            }
        }
        return res;
    }
};

