class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = { c: [] for c in range(numCourses) }

        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        # a course has three possible states
        # visited -> has been added
        # visiting -> added to cycle, not to output yet
        # unvisited -> neither output or cycle
        res = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visit:
                return True
            
            cycle.add(crs)
            
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return res