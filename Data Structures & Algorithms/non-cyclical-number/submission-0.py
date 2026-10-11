class Solution:
    def isHappy(self, n: int) -> bool:
        #we know that the cycle is endless if we hit a number that we have seen before, because we are just gonna go back down that number and get where we are
        seen = set()
        curr_num = n

        while curr_num > 1:
            if curr_num in seen:
                return False
            else:
                seen.add(curr_num)
                new_num = 0

                digits = curr_num
                while digits > 0:
                    digit = digits % 10
                    new_num = new_num + (digit * digit)
                    digits = digits // 10
                curr_num = new_num
        return True