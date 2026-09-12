class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        import bisect

        n = len(intervals)

        arr = []
        for i in range(n):
            l, r, w = intervals[i]
            arr.append((r, l, w, i))

        arr.sort()

        ends = [x[0] for x in arr]

        prev = [0] * n

        for i in range(n):
            prev[i] = bisect.bisect_left(ends, arr[i][1], 0, i)

        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            r, l, w, idx = arr[i - 1]

            for k in range(1, 5):
                not_take = dp[i - 1][k]

                old_score, old_indices = dp[prev[i - 1]][k - 1]

                take = (
                    old_score + w,
                    tuple(sorted(old_indices + (idx,)))
                )

                if take[0] > not_take[0]:
                    dp[i][k] = take
                elif take[0] < not_take[0]:
                    dp[i][k] = not_take
                else:
                    dp[i][k] = min(take, not_take)

        return list(dp[n][4][1])