class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        #keeps track of letter to frequency
        counts = Counter(s)

        #keep track of the explored letters in the current substring
        explored = set()

        #keep track of the length of the current substring
        curr_letter_count = 0

        #go through each letter
        for c in s:
            #add letter to explored
            explored.add(c)

            #decrement count of letter in count map
            counts[c] -= 1
            #just remove from dict if count is 0
            if counts[c] == 0:
                counts.pop(c)
            
            #increment the number of letters in this substring
            curr_letter_count += 1

            #we can only add count to resulting array if
            #all explored letters have counts of 0
            all_explored = True
            for val in explored:
                if val in counts:
                    all_explored = False
            
            #if we have confirmed that all values have been explored
            #add count to array and reset curr_letter_count and explored values
            if all_explored:
                result.append(curr_letter_count)
                curr_letter_count = 0
                explored.clear()
        
        return result
        