class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = window = max_window = l = 0

        for r in range(len(customers)):
            if grumpy[r]:
                window += customers[r]
            else:
                satisfied += customers[r]
            
            if r - l + 1 > minutes:
                window -= customers[l] if grumpy[l] == 1 else 0
                l += 1
            
            max_window = max(max_window, window)

        return satisfied + max_window