class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Time: O(mn) | Space: O(mn)
        m, n = len(s), len(p)
        cache = {}  # Mapping (i, j) -> match

        def dfs(i: int, j: int) -> bool:
            if i >= m and j >= n:
                return True

            if j >= n:
                return False

            if i >= m:
                return j < n - 1 and p[j + 1] == "*" and dfs(i, j + 2)

            if (i, j) in cache:
                return cache[(i, j)]

            if j < n - 1 and p[j + 1] == "*":
                if p[j] == ".":
                    cache[(i, j)] = (
                        dfs(i, j + 2) or  # skip *
                        dfs(i + 1, j) or  # use * multiple times
                        dfs(i + 1, j + 2)  # use * once
                    )
                    return cache[(i, j)]

                cache[(i, j)] = (
                    dfs(i, j + 2) or  # skip *
                    s[i] == p[j] and (
                        dfs(i + 1, j) or  # use * multiple times
                        dfs(i + 1, j + 2)  # use * once
                    )
                )
                return cache[(i, j)]

            if p[j] == ".":
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            cache[(i, j)] = s[i] == p[j] and dfs(i + 1, j + 1)
            return cache[(i, j)]

        return dfs(0, 0)
