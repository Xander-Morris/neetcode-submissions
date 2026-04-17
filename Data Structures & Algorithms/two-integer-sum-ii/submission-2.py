class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        num_to_index = defaultdict(list)

        for i in range(len(numbers)):
            num = numbers[i]
            remaining = target - num

            if remaining in num_to_index:
                return [num_to_index[remaining] + 1, i + 1]

            num_to_index[num] = i

        return result