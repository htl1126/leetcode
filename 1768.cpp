// Ref: https://leetcode.com/problems/merge-strings-alternately/solutions/1075534/java-c-python-straignt-forward-solutions/

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string res;
        int n = word1.size(), m = word2.size(), i = 0, j = 0;
        while (i < n || j < m) {
            if (i < n) {
                res.push_back(word1[i++]);
            }
            if (j < m) {
                res.push_back(word2[j++]);
            }
        }
        return res;
    }
};
