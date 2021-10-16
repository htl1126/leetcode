func minMovesToSeat(seats []int, students []int) int {
    sort.Ints(seats)
    sort.Ints(students)
    ans := 0
    for i := 0; i < len(seats); i++ {
        if seats[i] > students[i] {
            ans += seats[i] - students[i]
        } else {
            ans += students[i] - seats[i]
        }
    }
    return ans
}
