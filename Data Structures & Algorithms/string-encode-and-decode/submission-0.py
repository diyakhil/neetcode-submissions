class Solution:

    def encode(self, strs: List[str]) -> str:
        #add length of word + hash before the word when encoding
        res = ""

        for _str in strs:
            count = len(_str)
            encode = str(count) + '#' + _str

            res += encode
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            num = int(s[i:j])

            word = ""
            #in range is exclusive
            for k in range(j+1, j+1+num):
                word += s[k]
            
            res.append(word)

            #next i will be inclusive
            i = j + 1 + num
        
        return res

            

        
