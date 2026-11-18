class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = n

                for d in range(1, length):
                    if length % d == 0:
                        changes = 0

                        for x in range(d):
                            left = i + x
                            right = j - d + 1 + x

                            while left < right:
                                if s[left] != s[right]:
                                    changes += 1

                                left += d
                                right -= d

                        best = min(best, changes)

                cost[i][j] = best

        dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):
                for j in range(2 * (p - 1), i - 1):
                    dp[p][i] = min(
                        dp[p][i],
                        dp[p - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]