// Ref: https://leetcode.com/problems/count-submatrices-with-all-ones/discuss/721999/Python3-O(MN)-histogram-model

class Solution {
public:
    int numSubmat(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] != 0 && i - 1 >= 0) {
                    mat[i][j] += mat[i - 1][j];
                }
            }
        }
// cnt = (# of all-1 matrices with rightmost bottom at (i, 0))
//      +(# of all-1 matrices with rightmost bottom at (i, 1))
//      ...
//      +(# of all-1 matrices with rightmost bottom at (i, j))
//
// (')marked 1's are 'removed' from Step 1 to Step 2
// (*)marked 1's are 'removed' from Step 2 to Step 3
//
//   Step 1        Step 2          Step 3
//
//       1             1'
//   1 1 1         1'1'1'
//   1 1 1  1      1 1 1 1         1*1*1*1*
// 1 1 1 1  1 => 1 1 1 1 1    => 1*1*1*1*1*
// 1 1 1 1  1    1 1 1 1 1  1    1 1 1 1 1 1
//
// stack=        stack=          stack=
// [0 1 2 3]     [0 4]           [0 5]
//
// ans=          ans=            ans=
//  2             2               2
// +2+4          +2+4            +2+4
// +2+4+4        +2+4+4          +2+4+4
// +2+4+4+5      +2+4+4+5        +2+4+4+5
//               +2+3+3+3+3      +2+3+3+3+3
//                 ^^^^^^        +1+1+1+1+1+1
//                               ^^^^^^^^^^
// The code
//   count -= (mat[i][x] - mat[i][j]) * (x - y)
// is used to 'correct' the cumulative sum
        int ans = 0, count = 0, x, y;
        vector<int> stack;
        for (int i = 0; i < m; i++) {
            stack.clear();
            count = 0;
            for (int j = 0; j < n; j++) {
                while (!stack.empty() && mat[i][stack.back()] > mat[i][j]) {
                    x = stack.back();
                    stack.pop_back();
                    y = stack.empty() ? -1 : stack.back();
                    count -= (mat[i][x] - mat[i][j]) * (x - y);
                }
                count += mat[i][j];
                ans += count;
                stack.push_back(j);
            }
        }
        return ans;
    }
};
