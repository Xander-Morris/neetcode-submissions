class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()

        def backtrack(i, sub, total):
            if total == target:
                res.add(tuple(sub))
                return
            elif i >= len(candidates) or total > target:
                return
            
            sub.append(candidates[i])
            backtrack(i + 1, sub, total + candidates[i])
            sub.pop()
            backtrack(i + 1, sub, total)

        backtrack(0, [], 0)

        return [list(comb) for comb in res]