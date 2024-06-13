import networkx as nx
import matplotlib.pyplot as plt
import os

def convert_coordinates_to_numbers(coordinates):
    # Create the reverse mapping
    reverse_mapping = {
        (0, 3): 0, (1, 3): 1, (2, 3): 2, (3, 3): 3,
        (0, 2): 4, (1, 2): 5, (2, 2): 6, (3, 2): 7,
        (0, 1): 8, (1, 1): 9, (2, 1): 10, (3, 1): 11,
        (0, 0): 12, (1, 0): 13, (2, 0): 14, (3, 0): 15
    }
    
    # Convert the list of coordinates to numbers using the reverse mapping
    nums = [reverse_mapping[coord] for coord in coordinates]
    
    return nums


def create_adjacency_matrix():
    size=4
    """Initialize an adjacency matrix for a grid of given size."""
    num_vertices = size * size
    return [[0] * num_vertices for _ in range(num_vertices)]


def add_edge(adj_matrix, i, j):
    """Add an edge to the adjacency matrix."""
    adj_matrix[i][j] = 1
    adj_matrix[j][i] = 1  # For undirected graph


def pattern_to_adjacency_matrix(pattern):
    """Convert a pattern to an adjacency matrix."""
    adj_matrix = create_adjacency_matrix()
    for i in range(len(pattern) - 1):
        add_edge(adj_matrix, pattern[i], pattern[i + 1])
    return adj_matrix


def visualize_adjacency_matrix(adj_matrix):
    size=4
    """Visualize the adjacency matrix using networkx and matplotlib."""
    G = nx.Graph()
    num_vertices = size * size
    
    # Add nodes
    for i in range(num_vertices):
        G.add_node(i, pos=(i % size, size - (i // size)))
    
    # Add edges
    for i in range(num_vertices):
        for j in range(num_vertices):
            if adj_matrix[i][j] == 1:
                G.add_edge(i, j)
    
    pos = nx.get_node_attributes(G, 'pos')
    
    # Adjust figure size
    plt.figure(figsize=(2, 2))
    
    
    nx.draw(G, pos, with_labels=True, node_size=350, node_color='skyblue', font_weight='bold')
    
    # # Create the directory if it doesn't exist
    # if not os.path.exists('unique_pattern'):
    #     os.makedirs('unique_pattern')
    
    # # Save the figure in the unique_pattern directory
    # plt.savefig(f'unique_pattern/Pattern{i}.png')
    
    plt.show()



print("Helper Functions For Visualization Loaded Successfully!")
