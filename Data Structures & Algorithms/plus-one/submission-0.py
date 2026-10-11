class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        place = 1

        for i in range(len(digits) -1, -1, -1):
            number += digits[i] * place
            place = place * 10

        number += 1

        res = []

        while number > 0:
            digit = number % 10
            res.insert(0, digit)
            number = number // 10
        
        return res