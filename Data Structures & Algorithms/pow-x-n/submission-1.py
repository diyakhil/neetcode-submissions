class Solution:
    def myPow(self, x: float, n: int) -> float:
        cache = {}
        exp = abs(n)
        def helper(x, exp):
            if exp == 0:
                return 1
            if exp == 1:
                return x
            if exp in cache:
                return cache[exp]
            
            #else recurse, if exponent is event divide evenly by 2
            if exp % 2 == 0:
                res = helper(x, exp // 2) * helper(x, exp // 2)
                cache[exp] = res
                return res
            else:
                res = helper(x, exp // 2) * helper(x, exp // 2 + 1)
                cache[exp] = res
                return res
        
        total = helper(x, exp)
        if n < 0:
            return 1.0 / total
        else:
            return total
        
        