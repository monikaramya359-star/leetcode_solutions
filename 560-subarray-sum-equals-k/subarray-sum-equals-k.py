class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap={0:1}
        count=0
        prefix=0
        for num in nums:
            prefix+=num
            if prefix-k in hashmap:
                count+=hashmap[prefix-k]
            if prefix in hashmap:
                hashmap[prefix]+=1
            else:
                hashmap[prefix]=1
        return count
