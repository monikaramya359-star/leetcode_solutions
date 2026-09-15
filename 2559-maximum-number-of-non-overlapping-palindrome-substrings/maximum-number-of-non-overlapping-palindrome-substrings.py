class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        pal = [[False] * n for _ in range(n)]

        for i in range(n):
            pal[i][i] = True

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                if s[l] == s[r]:
                    if length == 2 or pal[l + 1][r - 1]:
                        pal[l][r] = True

        dp = [0] * (n + 1)

        for i in range(n):
            dp[i + 1] = dp[i]

            for j in range(i + 1):
                if i - j + 1 >= k and pal[j][i]:
                    dp[i + 1] = max(dp[i + 1], dp[j] + 1)

        return dp[n]
        