# Ref: https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/discuss/1223028/Python3-Stack

class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        ans = []
        while encoded1 and encoded2:
            val1, size1 = encoded1.pop()
            val2, size2 = encoded2.pop()
            val = val1 * val2
            if size1 < size2:
                encoded2.append([val2, size2 - size1])
            elif size1 > size2:
                encoded1.append([val1, size1 - size2])
            if ans and val == ans[-1][0]:  # faster than having ans = [[-1, -1]] in the beginning
                ans[-1][1] += min(size1, size2)
            else:
                ans.append([val, min(size1, size2)])
        return reversed(ans)  # faster than ans[::-1]
