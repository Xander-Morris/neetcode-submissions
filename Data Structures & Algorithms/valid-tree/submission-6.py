class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return False 
        if self.rank[root_i] < self.rank[root_j]:
            self.parents[root_i] = root_j
        elif self.rank[root_i] > self.rank[root_j]:
            self.parents[root_j] = root_i
        else:
            self.parents[root_i] = root_j
            self.rank[root_j] += 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dsu = DSU(n)
        components = n

        for a, b in edges:
            if not dsu.union(a, b):
                return False 
            components -= 1
        
        return components == 1