class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        visited = set([(x, y)])

        for p in path:
            if p == "N":
                y -= 1
            elif p == "S":
                y += 1
            elif p == "E":
                x += 1
            elif p == "W":
                x -= 1
            if (x, y) in visited:
                return True
            visited.add((x, y))

        return False 