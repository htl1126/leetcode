class Solution {
public:
    string decodeCiphertext(string encodedText, int rows) {
        int cols = encodedText.size() / rows;
        string res = "";
        for (int c = 0; c < cols; c++) {
            for (int i = 0; i < rows; i++) {
                if (c + i < cols) {
                    res += encodedText[i * cols + c + i];
                } else {
                    break;
                }
            }
        }
        while (res.back() == ' ') {
            res.pop_back();
        }
        return res;
    }
};
