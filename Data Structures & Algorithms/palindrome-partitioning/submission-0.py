class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #the backtracking in this will be like subsets

        res = []

        #curr_list is what in the partition currently
        #partitioned string is what is left to partition
        #index is where we left off the partition
        def helper(curr_list, index):
            if index > len(s) - 1:
                res.append(curr_list.copy()) #always append copy when backtracking
                return
            
            #now go through all of the parts left, ig that is just index to the end
            #want to go through all substrings so that will be index to i
            for i in range(index, len(s)):
                #check if they are palidromes only then append
                curr_str = s[index:i + 1] # do i+1 b/c i is not inclusive of last part
                
                if curr_str == curr_str[::-1]:
                    curr_list.append(curr_str)

                    #we use i + 1 b/c our first substring is index to i, so we want the next string to start at next partition
                    helper(curr_list, i + 1)

                    #we need to backtrack b/c in next iteration, curr_list will have a new whole chunk of word to start with
                    #not just the one we explored (eg. aa instead of a if word is aab)
                    curr_list.pop()
        
        helper([], 0)
        return res
        