// ref: https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/discuss/1525309/JavaC%2B%2BPython-DP-solution

func countMaxOrSubsets(nums []int) int {
    dp, max := [1 << 17]int{1}, 0
    for _, n := range nums {
        for i := max; i >= 0; i-- {
            dp[i | n] += dp[i]
        }
        max |= n
    }
    return dp[max]
}
