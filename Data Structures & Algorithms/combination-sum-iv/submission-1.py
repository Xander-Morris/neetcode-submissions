class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def _traverse(i, rem):
            if rem < 0:
                return

            if (i, rem) in memo:
                return memo[(i, rem)]

            res = 0

            if rem == 0:
                res += 1

            for j in range(len(nums)):
                if rem - nums[j] < 0:
                    continue

                res += _traverse(j, rem - nums[j])

            memo[(i, rem)] = res 

            return res

        return _traverse(0, target)