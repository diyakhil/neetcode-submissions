class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        
        seen_chars = set()

        left = 0
        right = 0

        while right < len(s):
            while s[right] in seen_chars:
                #now we need to close the window since a duplicate has been found
                #we need to keep closing the window until the char we are about to add is no longer there
                seen_chars.remove(s[left])
                left += 1
            
            #now that we know s[right] is not in seen chars alr we can add it to seen_chars
            seen_chars.add(s[right])

            #update the longest to be whatever is in seen_chars rn
            longest = max(longest, len(seen_chars))

            # now we need to update right, we just processed the prev iteration's right val
            right += 1
        
        return longest
        