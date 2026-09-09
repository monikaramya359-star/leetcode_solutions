class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0

        if n >= 1000:
            ans += (min(n, 999999) - 999)

        if n >= 1000000:
            ans += (min(n, 999999999) - 999999) * 2

        if n >= 1000000000:
            ans += (min(n, 999999999999) - 999999999) * 3

        if n >= 1000000000000:
            ans += (min(n, 999999999999999) - 999999999999) * 4

        if n >= 1000000000000000:
            ans += (n - 999999999999999) * 5

        return ans