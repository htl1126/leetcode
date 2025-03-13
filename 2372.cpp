class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        int row = grid.size(), col = grid[0].size();
        vector<vector<int>> res(row - 2, vector<int>(col - 2)),
            diff{{-1, -1}, {-1, 0}, {-1, 1},
                 {0, -1}, {0, 0}, {0, 1},
                 {1, -1}, {1, 0}, {1, 1}};

        for (int i = 0; i < row - 2; i++) {
            for (int j = 0; j < col - 2; j++) {
                int maxV = 0;
                for (int k = 0; k < 9; k++) {
                    int new_x = i + 1 + diff[k][0],
                        new_y = j + 1 + diff[k][1];
                    if (0 <= new_x && new_x < row && 0 <= new_y && new_y < col) {
                        maxV = max(maxV, grid[new_x][new_y]);
                    }
                }
                res[i][j] = maxV;
            }
        }

        return res;
    }
};

