class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        result = []

        for i in range(len(nums)):
            count[nums[i]] -= 1

            # "if i" means if i is greater than 0, since 0 is a falsy value.
            if i and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1

                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue

                target = -(nums[i] + nums[j])

                if count[target] > 0:
                    result.append([nums[i], nums[j], target])
            
            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1

        return result