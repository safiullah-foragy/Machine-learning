from collections import deque

def bfs(start, adj, n):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        
        for child in adj[node]:
            if not visited[child]:
                visited[child] = True
                queue.append(child)

n = 5
adj = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

print("BFS: ", end='')
bfs(1, adj, n)
