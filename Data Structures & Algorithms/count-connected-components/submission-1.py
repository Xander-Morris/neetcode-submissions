class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [0] * n
    
    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]
    
    def union(self, i, j):
        i_find = self.find(i)
        j_find = self.find(j)
        if i_find == j_find:
            return False
        i_rank = self.rank[i]
        j_rank = self.rank[j]

        if i_rank == j_rank:
            self.parents[j_find] = self.parents[i_find]
            self.rank[i] += 1
        elif i_rank < j_rank:
            self.parents[i_find] = self.parents[j_find]
            self.rank[j] += 1
        else:
            self.parents[j_find] = self.parents[i_find]
            self.rank[i] += 1
        return True 

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        
        for a, b in edges:
            if dsu.union(a, b):
                res -= 1

        return res