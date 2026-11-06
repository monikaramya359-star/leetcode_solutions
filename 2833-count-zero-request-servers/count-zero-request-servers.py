
from typing import List
from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda a: a[1])
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        count = defaultdict(int)
        ans = [0] * len(queries)

        left = right = 0

        for q, idx in sorted_queries:
            start = q - x

            while right < len(logs) and logs[right][1] <= q:
                count[logs[right][0]] += 1
                right += 1

            while left < right and logs[left][1] < start:
                server = logs[left][0]
                count[server] -= 1

                if count[server] == 0:
                    del count[server]

                left += 1

            ans[idx] = n - len(count)

        return ans
