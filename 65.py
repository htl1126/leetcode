class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def check_int(num):
            return num and all(c.isdigit() for c in set(num))

        def check_float(num):
            return num.count('.') == 1 and len(num) > 1 and \
                all(check_int(part) for part in num.split('.') if part)
        s = s.strip()
        if any(c.isalpha() and c != 'e' for c in set(s)):
            return False
        parts = s.split('e')
        if len(parts) > 2 or '' in parts:
            return False
        parts = map(lambda x: x[x[0] in '+-':], parts)
        if (check_float(parts[0]) or check_int(parts[0])) and \
                (len(parts) == 1 or len(parts) == 2 and check_int(parts[1])):
            return True
        return False
