class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        nums = []
        reverse1 = num1[::-1]
        reverse2 = num2[::-1]

        place = []
        for c2 in reverse2:
            product = []
            carryover = 0
            for c1 in reverse1:
                curr_product = int(c1) * int(c2) + carryover

                base = curr_product % 10
                product.append(str(base))
                carryover = curr_product // 10
            
            res = ''.join(product)
            if carryover:
                nums.append(''.join(place) + res + str(carryover))
            else:
                nums.append(''.join(place) + res)
            place.append('0')

        i = 0
        res = []
        carryover = 0
        #while it is less than the largest value's length
        while i < len(nums[-1]):
            _sum = 0
            for num in nums:
                if i < len(num):
                    _sum += int(num[i])
            _sum += carryover
            res.append(str(_sum % 10))
            carryover = _sum // 10
            i += 1
        
        if carryover:
            result = ''.join(res) + str(carryover)
        else:
            result = ''.join(res)
        reverse = result[::-1]
        
        if reverse[0] == '0':
            return '0'
        return reverse
        