class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr_sum = res = 0
        for i in range(k):
            curr_sum += arr[i]
        
        def _check_if_pass():
            nonlocal res
            avg = curr_sum / k
            if avg >= threshold:
                res += 1
        
        _check_if_pass()
        for j in range(k, len(arr)):
            curr_sum -= arr[j - k]
            curr_sum += arr[j]
            print(curr_sum)
            _check_if_pass()

        return res