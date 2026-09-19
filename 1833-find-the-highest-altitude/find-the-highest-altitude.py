class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        s=0
        prefixsum=[]
        for i in gain:
            s=s+i
            prefixsum.append(s)
        return max(max(prefixsum),0)
        