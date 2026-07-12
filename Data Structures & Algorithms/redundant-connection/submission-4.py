class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i, j):
        if self.find(i) == self.find(j):
            return False 

        if self.rank[i] == self.rank[j]:
            self.rank[i] += 1
            self.parents[self.find(j)] = self.parents[self.find(i)]
        elif self.rank[i] < self.rank[j]:
            self.rank[j] += 1
            self.parents[self.find(i)] = self.parents[self.find(j)]
        else:
            self.rank[i] += 1
            self.parents[self.find(j)] = self.parents[self.find(i)]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges) + 1)

        for a, b in edges:
            # the first union to be redundant is the first redundant edge 
            # dsu is used here to check for when we no longer need to union nodes together to have a 
            # fully connected component
            if not dsu.union(a, b):
                return [a, b]
        
        return [0, 0]