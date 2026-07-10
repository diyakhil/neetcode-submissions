class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """

        #input: position array which is the starting mile oof car i, speed at which car i will go, and target the mile the cars would reach at the same time to be considered in the same fleet

        #output: a single int of how many different fleets there will be at the destination (a fleet is defined as cars that meet or catch up to each other at or before the target, and then travel together at the slower car's speed)

        stack = []

        pos_speed = []
        for i in range(len(position)):
            pos_speed.append((position[i], speed[i]))

        #have to sort positions b/c we want to start from the end (car closes to finish line) and move to start
        sorted_position = sorted(pos_speed)

        #fleet count will just be the length of whatever is left over in the stack
        for i in range(len(sorted_position) -1, -1, -1):
            
            position = sorted_position[i][0]
            speed = sorted_position[i][1]

            hours = (target - position) / float(speed)

            if not stack or stack[-1] < hours:
                stack.append(hours)

        return len(stack)
        