class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        while low<high:
            mid=(low+high)//2
            if canfinish(weights,days,mid):
                high=mid
            else:
                low=mid+1
        return low

def canfinish(weights,days,capacity):
    load=0
    req_days=1
    for weight in weights:
        if load+weight<=capacity:
            load+=weight
        else:
            req_days+=1
            load=weight
    return req_days<=days