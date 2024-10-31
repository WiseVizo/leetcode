class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        ln = len(digits) - 1
        for digit in digits:
            num = num + (digit * (10 ** ln)) 
            ln -= 1
        num = num + 1
        return [int(i) for i in str(num)]