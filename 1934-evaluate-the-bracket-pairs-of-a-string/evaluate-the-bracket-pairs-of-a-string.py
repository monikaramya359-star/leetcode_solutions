class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = {key: value for key, value in knowledge}

        ans = []
        i = 0

        while i < len(s):
            if s[i] == '(':
                j = s.find(')', i + 1)
                key = s[i + 1:j]

                if key in d:
                    ans.append(d[key])
                else:
                    ans.append('?')

                i = j + 1
            else:
                ans.append(s[i])
                i += 1

        return ''.join(ans)
        