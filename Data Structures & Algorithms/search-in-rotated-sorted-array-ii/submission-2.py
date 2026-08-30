class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums.sort()
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return True
            
            if nums[low] <= nums[mid]:
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[mid] < target:
                    high = mid - 1
                else:
                    low = mid + 1

        return False 