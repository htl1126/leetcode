func decodeCiphertext(encodedText string, rows int) string {
    cols, res := len(encodedText) / rows, []byte{}
    for c := 0; c < cols; c++ {
        for i := 0; i < rows; i++ {
            if c + i < cols {
                res = append(res, encodedText[i * cols + c + i])
            }
        }
    }
    for i := len(res) - 1; i >= 0; i-- {
        if res[i] != ' ' {
            res = res[:i + 1]
            break
        }
    }
    return string(res)
}
