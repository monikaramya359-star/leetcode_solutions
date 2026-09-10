class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashmap={0:1}
        count=0
        pro=0
        for num in nums:
            pro+=num
            rem=pro%k
            if rem in hashmap:
                count+=hashmap[rem]
            if rem in hashmap:
                hashmap[rem]+=1
            else:
                hashmap[rem]=1
        return count

