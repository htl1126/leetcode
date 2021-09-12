func reversePrefix(word string, ch byte) string {
    i := strings.Index(word, string(ch));
    if i > -1 {
        s := []rune(word);
        for j := 0; j < i; j, i = j + 1, i - 1 {
            s[i], s[j] = s[j], s[i];
        }
        return string(s);
    }
    return word;
}
