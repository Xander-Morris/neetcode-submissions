class Solution:
    def hammingWeight(self, n: int) -> int:
        res = ""

        while n > 0:
            bit = n % 2
            n //= 2
            res += str(bit)
        
        res = res[::-1]

        return sum(1 if c == '1' else 0 for c in res)