class Solution {
public:
    string reversePrefix(string word, char ch) {
        size_t i = word.find(ch);
        if (i != string::npos) {
            size_t j = 0;
            while (j < i) {
                swap(word[j], word[i]);
                j++, i--;
            }
            return word;
        }
        return word;
    }
};
