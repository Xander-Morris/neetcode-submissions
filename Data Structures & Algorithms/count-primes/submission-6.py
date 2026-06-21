class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [False] * n
        res = 0

        for num in range(2, n):
            if sieve[num]:
                continue

            res += 1

            if num * num > n:
                continue

            for i in range(num * num, n, num):
                sieve[i] = True

        return res