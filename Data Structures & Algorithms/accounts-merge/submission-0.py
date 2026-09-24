class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]
        self.ranks = [0] * n
    
    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]
    
    def union(self, i, j):
        i_find = self.find(i)
        j_find = self.find(j)

        if self.ranks[i_find] == self.ranks[j_find]:
            self.parents[i_find] = j_find
        elif self.ranks[i_find] < self.ranks[j_find]:
            self.ranks[j_find] += 1
            self.parents[i_find] = j_find
        else:
            self.ranks[i_find] += 1
            self.parents[j_find] = i_find

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dsu = DSU(n)
        email_to_index = {}
        index_to_emails = {}

        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                if account[j] in email_to_index:
                    parent = email_to_index[account[j]]
                    dsu.union(parent, i)
                else:
                    email_to_index[account[j]] = i 

        for i, account in enumerate(accounts):
            parent = dsu.find(i)
            if parent not in index_to_emails:
                index_to_emails[parent] = set()
            for j in range(1, len(account)):
                index_to_emails[parent].add(account[j])

        res = []

        for index, emails in index_to_emails.items():
            new = []
            new.append(accounts[index][0])
            new.extend(sorted(list(emails)))
            res.append(new)

        return res