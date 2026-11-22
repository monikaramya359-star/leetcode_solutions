class Solution:
    def checkString(self, s: str) -> bool:
        seen = False
        for ch in s:
            if ch == 'b':
                seen = True
            elif seen:
                return False
        return True