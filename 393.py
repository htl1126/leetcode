class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        num_byte_mask = {1: 1 << 1}
        size = len(data)
        for i in range(2, 5):
            num_byte_mask[i] = (num_byte_mask[i - 1] | 1) << 1
        i = 0
        while i < size:
            if data[i] >> 7 == 0:
                i += 1
            else:
                if data[i] >> 6 == num_byte_mask[1]:
                    return False
                j = 2
                max_utf8_size = min(4, size - i)
                while j <= max_utf8_size:
                    if num_byte_mask[j] == (data[i] >> (7 - j)):
                        break
                    j += 1
                if j > max_utf8_size:
                    return False
                for k in range(i + 1, i + j):
                    if (data[k] >> 6) & 2 != 2:
                        return False
                i += j
        return True

if __name__ == '__main__':
    sol = Solution()
    testcase = [[197, 130, 1], [235, 140, 4], [145]]
    for i in xrange(3):
        print i, testcase[i]
        print sol.validUtf8(testcase[i])
