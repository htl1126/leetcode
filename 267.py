import collections


class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ctr = collections.Counter(s)
        if len([freq for freq in ctr.values() if freq & 1 == 1]) > 1:
            return []
        char, center = [], ''
        for k in ctr:
            if ctr[k] % 2 == 0:
                char += k * (ctr[k] / 2)
            else:
                char += k * ((ctr[k] - 1) / 2)
                center = k
        char.sort()
        ans = [[]]
        for c in char:
            new_ans = []
            for l in ans:
                for i in xrange(len(l) + 1):
                    new_ans.append(l[:i] + [c] + l[i:])
                    if i < len(l) and l[i] == c:
                        break
            ans = new_ans
        return [''.join(ans_i) + center + ''.join(ans_i)[::-1] for ans_i in ans]

if __name__ == '__main__':
    sol = Solution()
    testset = ['aabb', 'abc', 'a', 'aabbccc']
    for i, case in enumerate(testset):
        print i, case
        print sol.generatePalindromes(case)
