from collections import deque

def get_graph():
    graph = {}
    num = int(input())
    for _ in range(num):
        a, b = input().split()
        graph.setdefault(a, []).append(b)
    return graph

def find_path(graph, start, end):
    seen = set()
    q = deque([[start]])
    if start == end:
        return [start]
    while q:
        path = q.popleft()
        last = path[-1]
        if last not in seen:
            for nxt in graph.get(last, []):
                new = path + [nxt]
                q.append(new)
                if nxt == end:
                    return new
            seen.add(last)
    return None

def bfs_all(graph, start):
    seen = set()
    q = deque([start])
    res = []
    while q:
        node = q.popleft()
        if node not in seen:
            seen.add(node)
            res.append(node)
            q.extend(graph.get(node, []))
    return res

def main():
    g = get_graph()
    st = input()
    ed = input()
    ch = input()
    if ch == '1':
        ans = find_path(g, st, ed)
        print(" -> ".join(ans) if ans else "No path found")
    elif ch == '2':
        out = bfs_all(g, st)
        print(" -> ".join(out))

if __name__ == "__main__":
    main()
