// ref: https://leetcode.com/problems/largest-submatrix-with-rearrangements/solutions/1020710/c-clean-and-clear-with-intuitive-pictures-o-m-n-logn/
class Solution {
public:
    int largestSubmatrix(vector<vector<int>>& matrix) {
        int row = matrix.size(), col = matrix[0].size();
        int ans = 0;
        vector<int> height(col, 0);

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == 1) {
                    height[j]++;
                } else {
                    height[j] = 0;
                }
            }

            vector<int> ordered_height = height;
            sort(ordered_height.begin(), ordered_height.end());

            for (int j = 0; j < col; j++) {
                ans = max(ans, ordered_height[j] * (col - j));
            }
        }

        return ans;
    }
};

