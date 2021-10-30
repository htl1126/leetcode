// ref: https://leetcode.com/problems/minimum-distance-between-bst-nodes/discuss/?currentPage=1&orderBy=most_votes&query=

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func minDiffInBST(root *TreeNode) int {
    pre, res := -1, math.MaxInt32
    find := func (node *TreeNode) {}
    find = func (node *TreeNode) {
        if node.Left != nil {
            find(node.Left)
        }
        if pre >= 0 {
            if node.Val - pre < res {
                res = node.Val - pre
            }
        }
        pre = node.Val
        if node.Right != nil {
            find(node.Right)
        }
    }
    find(root)
    return res
}
