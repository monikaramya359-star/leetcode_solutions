class Solution:
    def countCommas(self, n: int) -> int:
        if len(str(n))<4:
            return 0
        else:
            return n+1-1000
