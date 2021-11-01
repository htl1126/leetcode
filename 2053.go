func kthDistinct(arr []string, k int) string {
    m := make(map[string]int)
    for _, s := range arr {
        m[s]++;
    }
    for _, s := range arr {
        if m[s] == 1 {
            k--;
            if k == 0 {
                return s
            }
        }
    }
    return "";
}
