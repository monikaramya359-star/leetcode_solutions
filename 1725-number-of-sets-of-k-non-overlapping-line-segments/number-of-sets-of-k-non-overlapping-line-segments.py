class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        dp = [[0] * (k + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = 1

        for j in range(1, k + 1):
            total = 0

            for i in range(n):
                if i > 0:
                    total += dp[i - 1][j - 1]
                    total %= MOD

                if i > 0:
                    dp[i][j] = dp[i - 1][j]

                if i >= 1:
                    dp[i][j] += total
                    dp[i][j] %= MOD

        return dp[n - 1][k]

        