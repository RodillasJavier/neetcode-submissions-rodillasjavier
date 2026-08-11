class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        in:
            - int array prerequisites
                - prerequisites[i] = [a, b] => must take 'b' before 'a'
            - int numCourses => how many you have to take
        out:
            - True if possible to finish all courses
            - False o/w
        constraints:
            - 1 <= numCourses <= 1000
            - 0 <= len(prerequisites) <= 1000
            - len(prerequisites[i]) == 2
            - 0 <= a[i], b[i] < numCourses
            - all pre req pairs are unique
        """
        crs_pre = {}
        for i in range(numCourses):
            crs_pre[i] = []
        
        for crs, pre in prerequisites:
            crs_pre[crs].append(pre)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False

            if crs_pre[course] == []:
                return True
            
            visited.add(course)

            for pre in crs_pre[course]:
                if dfs(pre) is False:
                    return False
                
            visited.remove(course)
            crs_pre[course] = []
        
        for course in range(numCourses):
            if dfs(course) is False:
                return False
        
        return True