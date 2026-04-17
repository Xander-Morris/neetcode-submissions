class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)

        def checkIfMatch(s2_count):
            for char in s1_count:
                if s2_count.get(char, 0) != s1_count.get(char, 0):
                    return False
            
            return True
        
        for i in range(len(s2) - len(s1) + 1):
            s2_count = {}
            s2_count[s2[i]] = 1

            for j in range(i + 1, i + len(s1)):
                s2_count[s2[j]] = 1 + s2_count.get(s2[j], 0)

            if checkIfMatch(s2_count):
                return True

        return False