class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [1] * n
    
    def find(self, i):
        while i != self.parents[i]:
            self.parents[i] = self.parents[self.parents[i]]
            i = self.parents[i]
        return i
    
    def union(self, i, j):
        i_find = self.find(i)
        j_find = self.find(j)

        if i_find == j_find:
            return False 

        if self.ranks[i_find] < self.ranks[j_find]:
            self.ranks[j_find] += self.ranks[i_find]
            self.parents[i_find] = j_find
        else:
            self.ranks[i_find] += self.ranks[j_find]
            self.parents[j_find] = i_find

        return True 

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dsu = DSU(n)
        email_to_index = {}
        index_to_emails = defaultdict(lambda: set())

        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                if account[j] in email_to_index:
                    parent = email_to_index[account[j]]
                    dsu.union(parent, i)
                else:
                    email_to_index[account[j]] = i 

        for i, account in enumerate(accounts):
            parent = dsu.find(i)
            for j in range(1, len(account)):
                index_to_emails[parent].add(account[j])

        res = []

        for index, emails in index_to_emails.items():
            res.append([accounts[index][0]] + sorted(emails))

        return res