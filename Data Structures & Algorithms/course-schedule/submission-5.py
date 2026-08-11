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

        def dfs(crs):
            if crs in visited:
                return False

            if crs_pre[crs] == []:
                return True

            visited.add(crs)

            for pre in crs_pre[crs]:
                if dfs(pre) is False:
                    return False

            visited.remove(crs)
            crs_pre[crs] = []

            return True

        for crs in range(numCourses):
            if dfs(crs) is False:
                return False

        return True


# time complexity: O(V + E)
# space complexity: O(V + E)
