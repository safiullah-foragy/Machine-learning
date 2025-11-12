def dfs_recursive(adj, visited, node):
    if visited[node]:
        return
    visited[node] = True
    print(node, end=' ')
    
    for child in adj[node]:
        if not visited[child]:
            dfs_recursive(adj, visited, child)

adj = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

visited = [False] * 6
print("DFS (Recursive): ", end='')
dfs_recursive(adj, visited, 2)
