class Solution:
    def isScramble(self, s1, s2):
        memo = {}

        def dp(a, b):
            if (a, b) in memo:
                return memo[(a, b)]

            if a == b:
                return True

            if sorted(a) != sorted(b):
                memo[(a, b)] = False
                return False

            n = len(a)

            for i in range(1, n):
                if dp(a[:i], b[:i]) and dp(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True

                if dp(a[:i], b[n-i:]) and dp(a[i:], b[:n-i]):
                    memo[(a, b)] = True
                    return True

            memo[(a, b)] = False
            return False

        return dp(s1, s2)