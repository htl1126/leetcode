class Solution {
public:
    bool winnerOfGame(string colors) {
        int a_count{0}, b_count{0};
        for (int i = 1; i < colors.size() - 1; i++) {
            if (colors[i - 1] == colors[i] && colors[i] == colors[i + 1]) {
                if (colors[i] == 'A') {
                    a_count++;
                } else {
                    b_count++;
                }
            }
        }
        return a_count > b_count;
    }
};
