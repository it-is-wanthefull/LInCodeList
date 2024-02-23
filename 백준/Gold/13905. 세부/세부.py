class DisjointSet:

    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        self.parent[root_x] = root_y


if __name__ == '__main__':
    from sys import stdin, setrecursionlimit

    input = stdin.readline
    setrecursionlimit(10 ** 5)

    n, m = map(int, input().split())
    s, e = map(int, input().split())
    bridge = []
    for _ in range(m):
        x, y, k = map(int, input().split())
        bridge.append((k, x, y))
    bridge.sort()
    djs = DisjointSet(n)
    last = 0
    while djs.find(s) != djs.find(e) and bridge:
        d, x, y = bridge.pop()
        last = d
        djs.union(x, y)
    print(last if djs.find(s) == djs.find(e) else 0)