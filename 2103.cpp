// Ref: https://leetcode.com/problems/rings-and-rods/solutions/1624277/bitmask-counter

class Solution {
public:
    int countPoints(string rings) {
        int rods[10] = {0};
        for (int i = 0; i < rings.size(); i += 2) {
            if (rings[i] == 'R') {
                rods[rings[i + 1] - '0'] |= 1;
            } else if (rings[i] == 'G') {
                rods[rings[i + 1] - '0'] |= 2;
            } else {
                rods[rings[i + 1] - '0'] |= 4;
            }
        }
        return count(begin(rods), end(rods), 7);
    }
};

