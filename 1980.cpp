// ref: https://leetcode.com/problems/find-unique-binary-string/solutions/1418687/detailed-explanation-o-n-java-c-python-short-concise-code-cantor-s-diagonalization/

class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        string ans = "";
        for (int i = 0; i < nums.size(); i++) {
            ans += nums[i][i] == '1' ? "0" : "1";
        }
        return ans;
    }
};

