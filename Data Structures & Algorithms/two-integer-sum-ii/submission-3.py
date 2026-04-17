class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = defaultdict(int)

        for i in range(len(numbers)):
            rem = target - numbers[i]

            if rem in mp:
                return [mp[rem] + 1, i + 1]
            
            mp[numbers[i]] = i

        return [0, 0]