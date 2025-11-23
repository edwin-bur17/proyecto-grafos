import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}  # adjacency list: node -> list of (neighbor, weight)

    def add_node(self, node):
        self.nodes.add(node)
        if node not in self.edges:
            self.edges[node] = []

    def add_edge(self, from_node, to_node, weight=1):
        self.add_node(from_node)
        self.add_node(to_node)
        self.edges[from_node].append((to_node, weight))
        self.edges[to_node].append((from_node, weight))  # undirected graph

    def shortest_path(self, start, end):
        # Return shortest path from start to end using Dijkstra's algorithm.
        queue = [(0, start, [])]
        visited = set()
        while queue:
            (cost, current, path) = heapq.heappop(queue)
            if current in visited:
                continue
            path = path + [current]
            if current == end:
                return path
            visited.add(current)
            for (neighbor, weight) in self.edges.get(current, []):
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor, path))
        return None  # no path found
