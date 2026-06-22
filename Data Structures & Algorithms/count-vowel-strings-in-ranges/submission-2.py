class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        vowels = ['a', 'e', 'i', 'o', 'u']

        for l, r in queries:
            to_add = 0

            for i in range(l, r + 1):
                word = words[i]

                if word[0] not in vowels or word[-1] not in vowels:
                    continue
                
                to_add += 1
        
            res.append(to_add)

        return res