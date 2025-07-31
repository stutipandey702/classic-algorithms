import sys
from collections import deque # for BFS

def init_graph(num_nodes, num_A_nodes, num_edges, G):
    # initialize the graph with the given edges
    for i in range(num_edges):
        src, dest = map(int, input().split())
        dest += num_A_nodes
        G[src * num_nodes + dest] = 1
    
    # connect source to all nodes in A
    for i in range(1, num_A_nodes + 1):
        G[0 * num_nodes + i] = 1
    
    # connect all nodes in  B to sink
    for i in range(num_A_nodes + 1, num_nodes - 1):
        G[i * num_nodes + (num_nodes - 1)] = 1

def bfs(num_nodes, G, path):
    # find augmenting path via BFS
    queue = deque([0])
    visited = [False] * num_nodes # all nodes unvisited at first
    visited[0] = True
    path[0] = -1
    
    while queue:
        current = queue.popleft()
        for next_node in range(num_nodes):
            if not visited[next_node] and G[current * num_nodes + next_node] > 0:
                queue.append(next_node)
                path[next_node] = current
                visited[next_node] = True
    
    return visited[num_nodes - 1]

def resid_capacity(num_nodes, G, path):
    # calculate residual capacity along augmenting path 
    flow = float('inf')
    v = num_nodes - 1
    
    # minimum residual capacity along path
    while path[v] != -1:
        u = path[v]
        flow = min(flow, G[u * num_nodes + v])
        v = u
    
    # update residual capacities
    v = num_nodes - 1
    while path[v] != -1:
        u = path[v]
        G[u * num_nodes + v] -= flow
        G[v * num_nodes + u] += flow
        v = u
    
    return flow

def max_flow(num_nodes, G):
    # compute maximum flow via Ford-Fulkerson 
    path = [-1] * num_nodes
    max_flow = 0
    
    while bfs(num_nodes, G, path):
        flow = resid_capacity(num_nodes, G, path)
        max_flow += flow
    
    return max_flow

def main():
    # handle input and output
    outputs = []
    num_instances = int(input())
    
    for _ in range(num_instances):
        num_nodes_A, num_nodes_B, num_edges = map(int, input().split())
        num_nodes_total = num_nodes_A + num_nodes_B + 2
        
        # init graph as a flattened 2D array
        graph = [0] * (num_nodes_total * num_nodes_total)
        
        init_graph(num_nodes_total, num_nodes_A, num_edges, graph)
        G_max_flow = max_flow(num_nodes_total, graph)
        
        result_char = 'Y' if num_nodes_A == num_nodes_B and G_max_flow == num_nodes_B else 'N'
        outputs.append(f"{G_max_flow} {result_char}")

    # print out all respective outputs
    for output in outputs:
        print(output)

if __name__ == "__main__":
    main()