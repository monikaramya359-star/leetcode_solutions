class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l=list(set(nums))
        if len(l)==0:
            return 0
        l.sort()
        c=1
        maxi=1
        for i in range(1,len(l)):
            if l[i]==l[i-1]+1:
                c=c+1
            else:
                c=1
            maxi=max(maxi,c)
        return maxi    