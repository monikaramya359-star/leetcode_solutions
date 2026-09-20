class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            value=ord('z')-ord(s[i])+1
            ans+=value*(i+1)
        return ans