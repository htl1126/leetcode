// Ref: https://leetcode.com/problems/check-if-n-and-its-double-exist/solutions/780188/faster-than-97-83-c

class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        unordered_set<int> set;
        for (const auto& n : arr) {
            if (set.count(2 * n) > 0 || !(n & 1) && set.count(n / 2) > 0) {
                return true;
            }
            set.insert(n);
        }
        return false;
    }
};

