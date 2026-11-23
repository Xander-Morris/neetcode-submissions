from collections import defaultdict 

class FreqStack:

    def __init__(self):
        self._st = []
        self._freq = defaultdict(int)
        self._max_freq = 0

    def push(self, val: int) -> None:
        self._st.append(val)
        self._freq[val] += 1
        self._max_freq = max(self._max_freq, self._freq[val])

    def pop(self) -> int:
        keys = set([key for key in self._freq.keys() if self._freq[key] == self._max_freq])
        j = 0

        for i in range(len(self._st) - 1, -1, -1):
            if self._st[i] in keys:
                j = i
                break

        val = self._st[j]
        self._st.pop(j)
        self._freq[val] -= 1
        self._max_freq = max(self._freq.values())

        return val 


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()