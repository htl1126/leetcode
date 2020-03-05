# Ref: https://leetcode.com/problems/invalid-transactions/discuss/366347/Simple-Python-Solution

class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        T = []
        for t in transactions:
            temp = t.split(',')
            temp[1] = int(temp[1])
            temp[2] = int(temp[2])
            T.append(temp)

        invalidT = []
        for t in T:
            if t[2] > 1000:
                t[1] = str(t[1])
                t[2] = str(t[2])
                invalidT.append(','.join(t))
                continue
            for x in T:
                if t[0] == x[0] and abs(t[1] - int(x[1])) <= 60 and t[3] != x[3]:                
                    t[1] = str(t[1])
                    t[2] = str(t[2])
                    invalidT.append(','.join(t))
                    break

        return invalidT

if __name__ == "__main__":
    sol = Solution()
    print sol.invalidTransactions()
