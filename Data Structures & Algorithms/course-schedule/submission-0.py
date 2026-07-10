class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        
        #first make an adjacency map using prequisite for easy access to courses
        for pre in prerequisites:
            adj_list[pre[0]].append(pre[1])
        

        def dfs(course, visited):
            #we reach a course with no prereqs - this is our breaking case in the prereq tree
            if adj_list[course] == []:
                return True
            
            res = True
            
            #we still need to keep visited b/c it's telling us the visited path for the current node
            visited.add(course)
            
            #now we recurse over the prereqs for the current course
            for pre_course in adj_list[course]:
                #return early if we know it fails at this set of prereqs
                if pre_course in visited:
                    return False
                
                if not dfs(pre_course, visited):
                    res = False
                
                #KEY: if we reach this stage we know the prereq is reachable for that particular course, so we can
                #remove that prereq from that course's dependency

                #since we are permanently altering the edge, it removes out need to back track
                adj_list[course].remove(pre_course)

            return res

        for i in range(numCourses):
            #reset visited set every time
            res = dfs(i, set())
        
            if not res:
                return False
        return True
        