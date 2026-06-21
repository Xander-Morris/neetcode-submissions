class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        count = Counter(nums)
        thresh = int(len(nums) / 3)

        for num in count:
            if count[num] > thresh:
                res.append(num)

        return res