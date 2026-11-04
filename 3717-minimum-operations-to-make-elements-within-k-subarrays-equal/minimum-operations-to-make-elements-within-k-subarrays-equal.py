
from typing import List
import heapq
from collections import Counter

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        low = []
        high = []
        deleted = Counter()

        low_size = 0
        high_size = 0
        low_sum = 0
        high_sum = 0

        def prune(heap, sign):
            while heap and deleted[sign * heap[0]] > 0:
                val = sign * heapq.heappop(heap)
                deleted[val] -= 1

        def balance():
            nonlocal low_size, high_size
            nonlocal low_sum, high_sum

            target = (low_size + high_size + 1) // 2

            while low_size > target:
                prune(low, -1)
                val = -heapq.heappop(low)
                heapq.heappush(high, val)
                low_size -= 1
                high_size += 1
                low_sum -= val
                high_sum += val

            while low_size < target:
                prune(high, 1)
                val = heapq.heappop(high)
                heapq.heappush(low, -val)
                low_size += 1
                high_size -= 1
                low_sum += val
                high_sum -= val

        def add(val):
            nonlocal low_size, high_size
            nonlocal low_sum, high_sum

            prune(low, -1)

            if not low or val <= -low[0]:
                heapq.heappush(low, -val)
                low_size += 1
                low_sum += val
            else:
                heapq.heappush(high, val)
                high_size += 1
                high_sum += val

            balance()

        def remove(val):
            nonlocal low_size, high_size
            nonlocal low_sum, high_sum

            prune(low, -1)
            prune(high, 1)

            deleted[val] += 1

            if val <= -low[0]:
                low_size -= 1
                low_sum -= val

                if val == -low[0]:
                    prune(low, -1)
            else:
                high_size -= 1
                high_sum -= val

                if high and val == high[0]:
                    prune(high, 1)

            balance()

        costs = []

        for i in range(n):
            add(nums[i])

            if i >= x:
                remove(nums[i - x])

            if i >= x - 1:
                median = -low[0]
                cost = median * low_size - low_sum
                cost += high_sum - median * high_size
                costs.append(cost)

        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(k + 1)]

        for i in range(n + 1):
            dp[0][i] = 0

        for j in range(1, k + 1):
            for i in range(1, n + 1):
                dp[j][i] = dp[j][i - 1]

                if i >= x:
                    dp[j][i] = min(
                        dp[j][i],
                        dp[j - 1][i - x] + costs[i - x]
                    )

        return dp[k][n]
