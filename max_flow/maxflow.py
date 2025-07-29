from collections import deque
import sys

def pathfind_bfs(num_nodes, graph, path):
    path[:] = [-1] * num_nodes
    visited = [False] * num_nodes # all nodes unvisited so far
    
    q = deque([0]) # implement BFS to find path
    visited[0] = True
    
    while q:
        u = q.popleft()
        
        for v in range(num_nodes):
            if graph[u][v] > 0 and not visited[v]:
                path[v] = u
                
                if v == num_nodes - 1:
                    return True
                
                q.append(v)
                visited[v] = True
    
    return False

def residual(num_nodes, graph, path):
    flow = float('inf') # set to a high number to start
    v = num_nodes - 1
    
    while path[v] >= 0:
        u = path[v]
        flow = min(flow, graph[u][v])
        v = u
    
    v = num_nodes - 1
    while path[v] >= 0:
        u = path[v]
        graph[u][v] -= flow
        graph[v][u] += flow
        v = u
    
    return flow

def max_flow(num_nodes, graph):
    path = [-1] * num_nodes
    max_flow = 0
    
    while pathfind_bfs(num_nodes, graph, path):
        max_flow += residual(num_nodes, graph, path)
    
    return max_flow

def main():
    num_instances = int(sys.stdin.readline().strip())
    outputs = []

    for _ in range(num_instances):
        num_nodes, num_edges = map(int, sys.stdin.readline().split())
        graph = [[0] * num_nodes for _ in range(num_nodes)]
        
        for _ in range(num_edges):
            src, dest, cap = map(int, sys.stdin.readline().split())
            graph[src - 1][dest - 1] += cap
        
        outputs.append(max_flow(num_nodes, graph))

    for output in outputs:
        print(output)

if __name__ == "__main__":
    main()
