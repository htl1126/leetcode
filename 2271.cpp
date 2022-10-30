// Ref: https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/discuss/2038534/Sliding-Window

class Solution {
public:
    int maximumWhiteTiles(vector<vector<int>>& tiles, int carpetLen) {
        int ans = 0, l = 0, cover = 0;
        sort(tiles.begin(), tiles.end());
        for (int r = 0; ans < carpetLen && r < tiles.size();) {
            if (tiles[l][0] + carpetLen > tiles[r][1]) {
                cover += tiles[r][1] - tiles[r][0] + 1;
                ans = max(ans, cover);
                r++;
            } else {
                int partial = max(0, tiles[l][0] + carpetLen - tiles[r][0]);
                ans = max(ans, cover + partial);
                cover -= tiles[l][1] - tiles[l][0] + 1;
                l++;
            }
        }
        return ans;
    }
};
