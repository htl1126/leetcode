class Solution(object):
    def __init__(self):
        self.res = []

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def get_ip(string, cur_ip):
            if len(cur_ip) == 4:
                if not string:
                    self.res += '.'.join(str(i) for i in cur_ip),
            else:
                for i in xrange(1, min(len(string) + 1, 4)):
                    if int(string[:i]) <= 255 and \
                            not (i > 1 and string[0] == '0') and \
                            len(string[i:]) <= 3 * (4 - len(cur_ip) - 1):
                        get_ip(string[i:], cur_ip + [int(string[:i])])
        get_ip(s, [])
        return self.res

if __name__ == '__main__':
    sol = Solution()
    print sol.restoreIpAddresses('25525511135')
