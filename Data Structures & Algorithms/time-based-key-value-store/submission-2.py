class TimeMap:

    def __init__(self):
        self.store = defaultdict(str)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.store:
            self.store[key] = defaultdict(str) 

        self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if not self.store[key]:
            return ""
        
        if self.store[key][timestamp]:
            return self.store[key][timestamp]
        
        for i in range(timestamp, 0, -1):
            if self.store[key][i]:
                return self.store[key][i]

        return ""