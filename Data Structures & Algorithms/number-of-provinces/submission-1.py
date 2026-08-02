class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = set()

        def _traverse(j):
            for i, num in enumerate(isConnected[j]):
                if num != 1:
                    continue
                if i in visited:
                    continue
                visited.add(i)
                _traverse(i)
        
        for i, inum in enumerate(isConnected):
            for j, jnum in enumerate(isConnected[i]):
                if jnum != 1:
                    continue
                
                if j in visited:
                    continue 

                visited.add(j)
                provinces += 1
                _traverse(j)

        return provinces