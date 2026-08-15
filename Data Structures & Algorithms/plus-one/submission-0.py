class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[len(digits) - 1] != 9:
            digits[len(digits) - 1] += 1
            return digits 

        digits[len(digits) - 1] = 0
        res = [0]
        carry = 1

        for i in range(len(digits) - 2, -1, -1):
            s = digits[i] + carry 
            
            if s <= 9:
                carry = 0
                res.append(s)
            else:
                carry = s % 9
                res.append(s % 10)

        if carry > 0:
            res.append(carry)

        res.reverse()

        return res