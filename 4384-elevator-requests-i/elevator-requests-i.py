class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        l=[]
        for i in range (1,len(requests)):
            a =abs(requests[i]-requests[i-1])
            l.append(a)
        l.append(requests[0])
        return sum(l)
            