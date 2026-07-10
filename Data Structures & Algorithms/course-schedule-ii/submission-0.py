class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_map = defaultdict(list)

        for pre in prerequisites:
            adj_map[pre[0]].append(pre[1])
        
        res = []

        #if course has already been visited then it has been included in the output
        visited = set()

        #if course is already in the curr_path that means we are about to form a cycle
        curr_path = set()
        
        def dfs(course):
            #we already have course in our result
            if course in visited:
                return True
            
            #course was already in our current path aka cycle is being formed
            if course in curr_path:
                return False
            
            curr_path.add(course)

            for pre in adj_map[course]:

                #we just detected a cycle
                if not dfs(pre):
                    return False
            curr_path.remove(course)

            #we went through all of the courses prereqs so we can now add it to visited
            visited.add(course)
            res.append(course)
            return True
            
        #call dfs on every cours
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res
        