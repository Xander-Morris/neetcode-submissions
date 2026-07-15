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
        
        if self.rank[i_find] > self.rank[j_find]:
            self.parents[j_find] = self.parents[i_find]
        elif self.rank[j_find] > self.rank[i_find]:
            self.parents[i_find] = self.parents[j_find]
        else:
            self.rank[i_find] += 1
            self.parents[j_find] = self.parents[i_find]

        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = n
        dsu = DSU(n)

        for a, b in edges:
            if dsu.union(a, b):
                components -= 1

        return components