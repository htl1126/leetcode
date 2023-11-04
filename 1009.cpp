// Ref: https://leetcode.com/problems/complement-of-base-10-integer/solutions/256740/java-c-python-find-111-1111-n

class Solution {
public:
    int bitwiseComplement(int n) {
        int i = 1;
        while (i < n) {
            i = i * 2 + 1;
        }
        return i - n;
    }
};

