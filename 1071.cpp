// ref: https://leetcode.com/problems/greatest-common-divisor-of-strings/solutions/3124940/c-one-line-beats-100-runtime-explanation


class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        return str1 + str2 == str2 + str1 ?
        str1.substr(0, gcd(str1.size(), str2.size())) :
        "";
    }
};

