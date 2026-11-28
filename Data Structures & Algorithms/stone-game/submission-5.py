from functools import cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def _max_alice_stones(l, r):
            if l >= r:
                return 0

            """
                what can happen:
                1. alice takes pile at piles[l], then bob takes pile at piles[l + 1]
                2. alice takes pile at piles[l], then bob takes pile at piles[r]
                3. alice takes pile at piles[r], then bob takes pile at piles[l]
                4. alice takes pile at piles[r], then bob takes pile at piles[r - 1]

                to simulate only max stones alice can achieve, we must account for skipping what bob can take
            """
            return max(
                piles[l] + _max_alice_stones(l + 2, r), 
                piles[l] + _max_alice_stones(l + 1, r - 1),
                piles[r] + _max_alice_stones(l + 1, r - 1),
                piles[r] + _max_alice_stones(l, r - 2),
            )

        return _max_alice_stones(0, len(piles) - 1) > sum(piles) // 2