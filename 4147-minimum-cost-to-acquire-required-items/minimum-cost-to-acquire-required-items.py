class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        a = need1 * cost1 + need2 * cost2

        b = max(need1, need2) * costBoth

        c = min(need1, need2) * costBoth

        c += (need1 - min(need1, need2)) * cost1
        c += (need2 - min(need1, need2)) * cost2

        return min(a, b, c)