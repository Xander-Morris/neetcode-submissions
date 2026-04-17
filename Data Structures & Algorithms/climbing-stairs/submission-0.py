class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n

        def dfs(i):
            if i >= n:
                return i == n # Only counts if it lands directly on the last step.

            if cache[i] != -1:
                return cache[i] # Return the cached calculation if it exists.

            # The total ways for this current step index is equal to
            # the ways from this step + 1 + the ways from this step + 2
            cache[i] = dfs(i + 1) + dfs(i + 2)

            return cache[i]

        return dfs(0)