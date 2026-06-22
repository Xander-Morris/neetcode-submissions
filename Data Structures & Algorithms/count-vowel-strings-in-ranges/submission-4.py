class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        pre_map = [0] * len(words)

        for i, word in enumerate(words):
            pre_map[i] = 0 if i == 0 else pre_map[i - 1]
            is_valid = word[0] in vowels and word[-1] in vowels
            pre_map[i] += 1 if is_valid else 0

        print(pre_map)

        for l, r in queries:
            to_add = pre_map[r] if l == 0 else pre_map[r] - pre_map[l - 1]
            res.append(to_add)

        return res