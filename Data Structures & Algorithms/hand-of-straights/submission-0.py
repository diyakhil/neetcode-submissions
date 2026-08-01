class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #case where we cannot arrange in buckets
        #this makes sure we have enough elements to fit make the groupSize for each group
        #weeds out early impossibility
        if len(hand) % groupSize > 0:
            return False
        
        buckets_len = len(hand) // groupSize

        #all we need to do is keep track of the counts of each bucket
        #makes value : freq map
        hand_hash = Counter(hand)
        counts = dict(sorted(hand_hash.items())) #sort based on keys or the actual values in the hand

        while counts:
            first_value = list(counts.keys())[0]

            #this ensures that once we hit the group size, aka the bucket is filled, we will move on to calculating
            #the next bucket
            for i in range(groupSize):
                #this automatically returns false if next consecurive number is not found
                if counts.get(first_value, 0) == 0:
                    return False
                
                counts[first_value] -= 1

                if counts[first_value] == 0:
                    counts.pop(first_value, None)

                first_value += 1
        return True
        