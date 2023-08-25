class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int ans = 0;
        for (int i = 0, j = 0; i < mat.size(); i++, j++) {
            if (j == mat.size() - 1 - j) {
                ans += mat[i][j];
            } else {
                ans += mat[i][j] + mat[i][mat.size() - 1 - j];
            }
        }
        return ans;
    }
};
