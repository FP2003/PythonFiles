

class Vertex:
    def __init__(self, n):
        self.name = n  # Initialize the name of the vertex
        self.neighbors = set()  # Initialize an empty set to store neighbor vertices
        
    def add_neighbors(self, v):
        self.neighbors.add(v)  # Add a neighbor vertex to the set of neighbors


class Graph:
    verticies = {}  # Initialize an empty dictionary to store vertices
    
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        
        Args:
            vertex (Vertex): The vertex to add to the graph.
        
        Returns:
            bool: True if the vertex is added successfully, False otherwise.
        """
        if isinstance(vertex, Vertex) and vertex.name not in self.verticies:
            self.verticies[vertex.name] = vertex  # Add the vertex to the dictionary of vertices
            return True
        else:
            return False
    
    def add_edge(self, u, v):
        """
        Add an edge between two vertices in the graph.
        
        Args:
            u (str): The name of the first vertex.
            v (str): The name of the second vertex.
        
        Returns:
            bool: True if the edge is added successfully, False otherwise.
        """
        if u in self.verticies and v in self.verticies:
            self.verticies[u].add_neighbors(v)  # Add v as a neighbor of u
            self.verticies[v].add_neighbors(u)  # Add u as a neighbor of v
            return True
        else:
            return False
        
    def print_graph(self):
        """
        Print the graph.
        """
        for key in sorted(list(self.verticies.keys())):
            print(key, sorted(list(self.verticies[key].neighbors)))  # Print each vertex and its neighbors
            
# Create a graph instance
g = Graph()

# Add vertices to the graph
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))
    
# Add edges to the graph
edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ']
for edge in edges:
    g.add_edge(edge[0], edge[1])

# Print the graph
g.print_graph()
