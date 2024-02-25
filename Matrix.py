class Vertex:
    def __init__(self, n):
        """
        Initialize a vertex with a name.
        
        Args:
            n: The name of the vertex.
        """
        self.name = n  # Initialize the name of the vertex

class Graph:
    verticies = {}  # Initialize an empty dictionary to store vertices
    edges = []      # Initialize an empty list to store edges
    edge_indices = {}  # Initialize an empty dictionary to store edge indices
    
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        
        Args:
            vertex (Vertex): The vertex to add to the graph.
        
        Returns:
            bool: True if the vertex is added successfully, False if it already exists.
        """
        if isinstance(vertex, Vertex) and vertex.name not in self.verticies:
            # Update verticies dictionary
            self.verticies[vertex.name] = len(self.verticies)
            
            # Update edges with a new row and column
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            
            # Update edge_indices dictionary
            self.edge_indices[vertex.name] = len(self.edge_indices)
            
            return True
        else:
            return False
        
    def add_edge(self, u, v, weight=1):
        """
        Add an edge between two vertices in the graph.
        
        Args:
            u (str): The name of the first vertex.
            v (str): The name of the second vertex.
            weight (int): The weight of the edge (default is 1).
        
        Returns:
            bool: True if the edge is added successfully, False otherwise.
        """
        if u in self.verticies and v in self.verticies:
            # Update the adjacency matrix
            self.edges[self.verticies[u]][self.verticies[v]] = weight
            self.edges[self.verticies[v]][self.verticies[u]] = weight
            return True
        else:
            return False
        
    def print_graph(self):
        """
        Print the adjacency matrix representation of the graph.
        """
        for v, i in sorted(self.edge_indices.items()):
            print(v + ' ', end='')  # Print vertex name
            for j in range(len(self.edges[i])):
                print(self.edges[i][j], end=' ')  # Print edge weight
            print('')  # Move to the next line
            
# Test the graph
g = Graph()

# Add vertices to the graph
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

# Add edges to the graph
edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HJ']
for edge in edges:
    g.add_edge(edge[0], edge[1])

# Print the graph
g.print_graph()
