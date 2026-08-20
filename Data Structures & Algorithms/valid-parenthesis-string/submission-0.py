class Solution:
    def checkValidString(self, s: str) -> bool:
        #store the indices of the chars rather than the chars themselves in the stacks
        star = []
        opening = []

        for i in range(len(s)):
            if s[i] == '*':
                star.append(i)
            if s[i] == '(':
                opening.append(i)
            
            if s[i] == ')':
                #if the index of the opening is less than the current index then pop from stack
                if opening and opening[0] < i:
                    opening.pop()
                elif star and star[0] < i:
                    star.pop()
                else:
                    #return because we cannot find a matching opening parenthesis for the closing
                    return False
        
        #need a while loop at the end for any leftover openings that can be resolved with a star
        #cannot use a for loop for the length of the element and then delete stuff b/c the length of the
        #list is then altered so we will get a bunch of index out of boud errors
        while opening and star and opening[-1] < star[-1]:
            opening.pop()
            star.pop()
    
        #only valid if there are no items left in opening - all openings have corresponding closings
        return len(opening) == 0
        