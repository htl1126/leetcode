class Solution {
    public String reversePrefix(String word, char ch) {
        int i = word.indexOf(ch);
        if (i != -1) {
            char[] s = word.toCharArray();
            char t;
            int j = 0;
            while (j < i) {
                t = s[i];
                s[i] = s[j];
                s[j] = t;
                j++;
                i--;
            }
            return new String(s);
        }
        return word;
    }
}
