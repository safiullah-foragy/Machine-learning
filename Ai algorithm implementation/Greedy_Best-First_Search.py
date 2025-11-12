import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5)],
    'C': [('D', 1)],
    'D': [('E', 3)],
    'E': []
}

h = {'A': 7, 'B': 6, 'C': 2, 'D': 1, 'E': 0}

def greedy_best_first(start, goal):
    pq = [(h[start], start)]
    visited = {}
    parent = {}
    
    while pq:
        _, node = heapq.heappop(pq)
        
        if node in visited:
            continue
            
        visited[node] = True
        print(node, end=' ')
        
        if node == goal:
            print("\nPath found:", end=' ')
            path = []
            v = node
            while v:
                path.append(v)
                v = parent.get(v)
            path.reverse()
            print(' '.join(path))
            return
        
        for nbr, cost in graph[node]:
            if nbr not in visited:
                heapq.heappush(pq, (h[nbr], nbr))
                parent[nbr] = node

print("Greedy Best First Search (A → E)")
greedy_best_first('A', 'E')
