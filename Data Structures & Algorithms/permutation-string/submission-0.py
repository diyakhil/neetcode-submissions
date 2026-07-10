class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        alpha = 'abcdefghijklmnopqrstuvwxyz'

        s1_hash = {}
        s2_hash = {}

        for c in alpha:
            s1_hash[c] = 0
            s2_hash[c] = 0
        
        #update freq of s1
        for c in s1:
            s1_hash[c] += 1

        left = 0
        right = 0
        
        while right < len(s2):
            #add curr value to hashset
            s2_hash[s2[right]] += 1

            #keep incrementing until we hit the length of the window we want, which is length of s1
            while right - left + 1 < len(s1):
                print(str(left) + ' ' + str(right))
                right += 1
                s2_hash[s2[right]] += 1

            
            #we have hit the window len, now we need to check if the hashes are equal and return
            if s1_hash == s2_hash:
                return True
            else:
                #first update hash_map w existing elem then update counts
                s2_hash[s2[left]] -= 1
                left += 1

                right += 1
        return False
        