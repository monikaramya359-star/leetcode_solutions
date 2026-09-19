class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        l=[]
        for car in nums:
            for i in range(car[0],car[1]+1):
                l.append(i)
        s=list(set(l))
        return len(s)