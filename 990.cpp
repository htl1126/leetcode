// Ref: https://leetcode.com/problems/satisfiability-of-equality-equations/discuss/234486/JavaC%2B%2BPython-Easy-Union-Find

class Solution {
public:
    int uf[26];
    int find(int x) {
        if (x != uf[x]) {
            uf[x] = find(uf[x]);
        }
        return uf[x];
    }

    bool equationsPossible(vector<string>& equations) {
        for (int i = 0; i < 26; i++) {
            uf[i] = i;
        }
        for (const string& s : equations) {
            if (s[1] == '=') {
                uf[find(s[0] - 'a')] = find(s[3] - 'a');
            }
        }
        for (const string& s : equations) {
            if (s[1] == '!' && find(s[0] - 'a') == find(s[3] - 'a')) {
                return false;
            }
        }
        return true;
    }
};
