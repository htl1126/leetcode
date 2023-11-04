class Solution {
public:
    string reverseStr(string s, int k) {
        for (int start = 0; start < s.size(); start += 2 * k) {
            int end = min(start + k - 1, (int)(s.size() - 1));
            for (int i = start, j = end; i < j; i++, j--) {
                swap(s[i], s[j]);
            }
        }
        return s;
    }
};

