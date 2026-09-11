class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = {}

        for x in digits:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        ans = 0

        for num in range(100, 1000):
            if num % 2 != 0:
                continue

            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            need = {}

            if a in need:
                need[a] += 1
            else:
                need[a] = 1

            if b in need:
                need[b] += 1
            else:
                need[b] = 1

            if c in need:
                need[c] += 1
            else:
                need[c] = 1

            possible = True

            for x in need:
                if x not in freq or need[x] > freq[x]:
                    possible = False
                    break

            if possible:
                ans += 1

        return ans