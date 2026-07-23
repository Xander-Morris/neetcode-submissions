class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        st = set()
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > n // 3:
                st.add(num)

        return list(st)