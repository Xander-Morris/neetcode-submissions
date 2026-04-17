class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, sub, total):
            if total == target:
                res.append(sub[:])
                return
            elif total > target or i >= len(candidates):
                return

            sub.append(candidates[i])
            backtrack(i + 1, sub, total + candidates[i])
            sub.pop()

            # While we encounter duplicates, keep going forward. 
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            backtrack(i + 1, sub, total)

        backtrack(0, [], 0)

        return res