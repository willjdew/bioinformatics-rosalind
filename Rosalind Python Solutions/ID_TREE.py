# http://rosalind.info/problems/tree/

# Given: A positive integer n (n≤1000) and an adjacency list corresponding to a
# graph on n nodes that contains no cycles.

# Return: The minimum number of edges that can be added to the graph to produce
# a tree.

# a tree can have at most n-1 edges. We simply count the number of edges, and
# subtract it from n−1. 
def connect_tree(n, adj_list):
    # Find the connected components of the graph.
    cc = n - len(adj_list)
    # Return the count of the components minus 1.
    return cc - 1
