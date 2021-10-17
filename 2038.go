func winnerOfGame(colors string) bool {
    a_count, b_count := 0, 0
    for i := 1; i < len(colors) - 1; i++ {
        if colors[i - 1] == colors[i] && colors[i] == colors[i + 1] {
            if colors[i] == 'A' {
                a_count++
            } else {
                b_count++
            }
        }
    }
    return a_count > b_count
}
