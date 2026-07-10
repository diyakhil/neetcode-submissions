class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        letter_freq = {}

        max_len = 0

        while right < len(s):
            #this is all calc from prev iteration after we incremented right

            #update the hash to process the current index
            letter_freq[s[right]] = letter_freq.get(s[right], 0) + 1
            
            while (right - left + 1) - max(letter_freq.values()) > k:
                #case where we need to decrease window size (adjust left)
                letter_freq[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
            right += 1
        
        return max_len
        