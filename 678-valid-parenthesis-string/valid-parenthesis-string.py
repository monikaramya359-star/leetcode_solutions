class Solution:
    def checkValidString(self, s: str) -> bool:
        open = []
        star = []

        for i in range(len(s)):
            if s[i] == '(':
                open.append(i)

            elif s[i] == '*':
                star.append(i)

            else:
                if open:
                    open.pop()
                elif star:
                    star.pop()
                else:
                    return False

        while open and star:
            if open[-1] > star[-1]:
                return False

            open.pop()
            star.pop()

        return len(open) == 0