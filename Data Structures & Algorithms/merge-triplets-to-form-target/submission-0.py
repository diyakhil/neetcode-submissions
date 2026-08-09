class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #keep track of an array of indices that we still need to find
        indices_left = [0, 1, 2]

        #iterate through each option (or problem) only once
        for triplet in triplets:

            #this means a value is greater than the target value so this triplet cannot be considered
            #as it will overshadow the target values (we are taking max each time)

            #tried doing this in a for loop and could not figure out the continue logic
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            for i in range(3):
                #make sure we are looking for i values we want to make up
                if i in indices_left and triplet[i] == target[i]:
                    indices_left.remove(i)
        
        if len(indices_left) == 0:
            return True
        else:
            return False
        