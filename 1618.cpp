// Ref: https://leetcode.com/problems/maximum-font-to-fit-a-sentence-in-a-screen/solutions/3644500/binary-search-hashtable/

/**
 * // This is the FontInfo's API interface.
 * // You should not implement it, or speculate about its implementation
 * class FontInfo {
 *   public:
 *     // Return the width of char ch when fontSize is used.
 *     int getWidth(int fontSize, char ch);
 *     
 *     // Return Height of any char when fontSize is used.
 *     int getHeight(int fontSize)
 * };
 */
class Solution {
    bool canFitScreen(int area_w, int area_h, vector<int> &freq, int fontSize, FontInfo &fontInfo) {
        int h = fontInfo.getHeight(fontSize);
        long long w_total = 0LL;
        for (char c = 'a'; c <= 'z'; c++) {
            w_total += freq[c - 'a'] * fontInfo.getWidth(fontSize, c);
        }

        return w_total <= area_w && h <= area_h;
    }
public:
    int maxFont(string text, int w, int h, vector<int>& fonts, FontInfo fontInfo) {
        vector<int> freq(26, 0);
        for (const auto& c : text) {
            freq[c - 'a']++;
        }

        int l = 0, r = fonts.size() - 1;
        while (l < r) {
            int m = (l + r + 1) / 2;
            if (canFitScreen(w, h, freq, fonts[m], fontInfo)) {
                l = m;
            } else {
                r = m - 1;
            }
        }

        // additional check for l == 0:
        // when l == 0 and r == 1 and m == 1, canFitScreen() fails,
        // r will be updated to 0 and the while loop terminates.
        // However, in this situation we haven't checked fonts[0] yet.
        if (l > 0 || canFitScreen(w, h, freq, fonts[0], fontInfo)) {
            return fonts[l];
        }

        return -1;
    }
};

