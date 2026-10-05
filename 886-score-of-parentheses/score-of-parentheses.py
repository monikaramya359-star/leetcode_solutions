class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                x = stack.pop()

                if x == 0:
                    x = 1
                else:
                    x = 2 * x

                stack[-1] += x

        return stack[0]