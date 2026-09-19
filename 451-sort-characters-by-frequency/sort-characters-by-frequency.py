class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for ch in s:
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
        ans=""
        for i in range(1,len(s)+1):
            for ch in d:
                if d[ch]==i:
                    ans=ch*i+ans
        return ans