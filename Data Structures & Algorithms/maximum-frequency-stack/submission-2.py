from collections import defaultdict 

class FreqStack:

    def __init__(self):
        self._st = []
        self._freq = defaultdict(int)

    def push(self, val: int) -> None:
        self._st.append(val)
        self._freq[val] += 1

    def pop(self) -> int:
        max_freq = max(self._freq.values())
        keys = set([key for key in self._freq.keys() if self._freq[key] == max_freq])
        j = 0

        for i in range(len(self._st) - 1, -1, -1):
            if self._st[i] in keys:
                j = i
                break

        val = self._st[j]
        self._st.pop(j)
        self._freq[val] -= 1

        return val 


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()