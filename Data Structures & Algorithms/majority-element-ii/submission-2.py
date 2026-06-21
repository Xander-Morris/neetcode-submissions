class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        thresh = int(len(nums) / 3)

        return [num for num in count if count[num] > thresh]