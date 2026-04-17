class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return m

            # Left sorted portion
            if nums[m] >= nums[l]:
                if nums[m] < target or nums[l] > target:
                    l = m + 1
                else:
                    r = m - 1
            # Right Sorted portion
            else:
                if nums[m] > target or nums[r] < target:
                    r = m - 1
                else:
                    l = m + 1

        return -1