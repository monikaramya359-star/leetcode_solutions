class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c=0
        for i in stones:
            if i in jewels:
                c+=1
        return c