class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set([n])

        while n > 1:
            new_n = n
            s = 0

            while new_n > 0:
                dig = new_n % 10
                s += pow(dig, 2)
                new_n //= 10
            
            n = s

            if n in seen:
                return False

            seen.add(n)

        return n == 1