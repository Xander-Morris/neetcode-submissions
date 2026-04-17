class TimeMap:

    def __init__(self):
        self.store = defaultdict(str)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.store:
            self.store[key] = defaultdict(str)
            self.store[key]["direct"] = defaultdict(str)
            self.store[key]["composite"] = []

        self.store[key]["direct"][timestamp] = value
        self.store[key]["composite"].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        if self.store[key]["direct"][timestamp]:
            return self.store[key]["direct"][timestamp]
        
        times = self.store[key]["composite"]
        left = 0
        right = len(times) - 1
        result = ""

        while left <= right:
            middle = (left + right) // 2

            if times[middle][0] <= timestamp:
                result = times[middle][1]
                left = middle + 1
            else:
                right = middle - 1

        return result