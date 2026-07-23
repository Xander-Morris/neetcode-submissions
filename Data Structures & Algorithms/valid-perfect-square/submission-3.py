class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True 
        for i in range(1, num // 2):
            if i * i == num:
                return True
        return False