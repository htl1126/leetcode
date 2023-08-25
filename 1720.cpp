// Ref: https://leetcode.com/problems/decode-xored-array/solutions/1009844/java-c-python-easy-and-concise

class Solution {
public:
    vector<int> decode(vector<int>& encoded, int first) {
        int cur = first;
        vector<int> res = {cur};
        for (int& a: encoded)
            res.push_back(cur ^= a);
        return res;
    }
};
