class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        l=0
        r=len(letters)-1
        ans=letters[0]
        while l<=r:
            mid=(l+r)//2
            if letters[mid] >target:
                ans=letters[mid]
                r=mid-1
            else:
                l=mid+1
        return ans