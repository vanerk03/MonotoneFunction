# time complexity of the algorithm is O(k * log k) = O(k * n)
# k = 2 ** n
# n - arity of boolean function

def isMonotone(n: int, vector: str) -> bool:

    used = [False] * (2 ** n)

    def dfs(s):

        res = True
        copyS = s
        used[s] = True
        now = 1

        for _ in range(n):

            bit = copyS % 2
            copyS //= 2

            if bit == 0:
                if int(vector[now + s]) < int(vector[s]):
                    return False
                if not used[now + s]:
                    res = res and dfs(now + s)

            now *= 2
        return res

    return dfs(0)
