class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        ip4 = IP.split('.')
        if len(ip4) == 4 and all(c.isdigit() and
                                 not (len(c) > 1 and c[0] == '0') for c in ip4)\
           and all(int(c) < 256 for c in ip4):
            return 'IPv4'
        ip6 = IP.upper().split(':')
        if len(ip6) == 8 and all(1 <= len(s) <= 4 and\
                                 all(c in '0123456789ABCDEF' for c in s) for s in ip6):
            return 'IPv6'
        return 'Neither'


if __name__ == '__main__':
    sol = Solution()
    print sol.validIPAddress('256.256.256.256')
