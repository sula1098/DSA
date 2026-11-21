
class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)
        sign = 1
        num = 0

        while i < n and s[i] == ' ':
            i += 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        while i < n and '0' <= s[i] <= '9':
            num = num * 10 + (ord(s[i]) - ord('0'))
            i += 1

        num *= sign

        num = max(-2**31, min(num, 2**31 - 1))

        return num
