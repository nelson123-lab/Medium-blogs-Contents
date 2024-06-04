## Components of Graph Network

1. **Vertices (Nodes):**
   - The fundamental units or points in a graph. The number of vertices in a graph is denoted as \( |V| \) or \( n \).

2. **Edges (Links):** 
    - Connections between pairs of vertices. The number of edges in a graph is denoted as \( |E| \) or \( m \).
3. **Degree:**
   - **Degree of a Vertex:** The number of edges incident to a vertex.
   - **In-Degree:** For directed graphs, the number of edges coming into a vertex.
   - **Out-Degree:** For directed graphs, the number of edges going out of a vertex.
   - **Degree Sequence:** A list of the degrees of the vertices, usually in non-increasing order.

4. **Paths and Cycles:**
   - **Path:** A sequence of vertices where each adjacent pair is connected by an edge.
   - **Cycle:** A path that starts and ends at the same vertex and includes no other repeated vertices.

5. **Connectivity:**
   - **Connected Graph:** A graph where there is a path between every pair of vertices.
   - **Strongly Connected:** In directed graphs, if there is a directed path from any vertex to every other vertex.
   - **Weakly Connected:** In directed graphs, if replacing all directed edges with undirected edges makes the graph connected.

6. **Subgraphs:**
   - **Induced Subgraph:** A graph formed by a subset of vertices and all the edges between them.
   - **Spanning Subgraph:** A subgraph that includes all the vertices of the original graph.

7. **Components:**
   - **Connected Components:** Maximal connected subgraphs.
   - **Biconnected Components:** Maximal biconnected subgraphs, meaning removing any single vertex won't disconnect the component.

8. **Adjacency:**
   - **Adjacency Matrix:** A square matrix used to represent a finite graph. The element at row \( i \) and column \( j \) is 1 (or the weight of the edge) if there is an edge from vertex \( i \) to vertex \( j \), otherwise 0.
   - **Adjacency List:** A collection of lists or arrays, one per vertex, listing all adjacent vertices.

9. **Graph Types:**
   - **Simple Graph:** A graph with no loops (edges connected at both ends to the same vertex) and no multiple edges between the same pair of vertices.
   - **Multigraph:** A graph which is allowed to have multiple edges (that is, edges that have the same end nodes).
   - **Directed Graph (Digraph):** A graph where edges have a direction, going from one vertex to another.
   - **Undirected Graph:** A graph where edges have no direction.
   - **Weighted Graph:** A graph where edges have weights or costs associated with them.
   - **Bipartite Graph:** A graph whose vertices can be divided into two disjoint and independent sets \( U \) and \( V \) such that every edge connects a vertex in \( U \) to one in \( V \).

10. **Special Graphs:**
    - **Complete Graph (K_n):** A graph where there is an edge between every pair of vertices.
    - **Cycle Graph (C_n):** A graph that consists of a single cycle, or in other words, some number of vertices connected in a closed chain.
    - **Tree:** An acyclic connected graph.
    - **Forest:** A disjoint set of trees.
    - **Planar Graph:** A graph that can be embedded in the plane, i.e., it can be drawn on a plane without edge crossings.

11. **Graph Invariants:**
    - **Chromatic Number:** The minimum number of colors needed to color the vertices so that no two adjacent vertices share the same color.
    - **Clique Number:** The size of the largest complete subgraph.
    - **Radius and Diameter:**
      - **Radius:** The minimum eccentricity of any vertex.
      - **Diameter:** The maximum eccentricity of any vertex.
    - **Eccentricity:** The greatest distance from a vertex to any other vertex.

## Metrics used in Graph Analysis

1. **Degree Centrality:**
   - **Definition:** The number of edges connected to a vertex.
   - **Use:** Indicates the importance or influence of a vertex within the graph.
   - **Types:**
     - **In-Degree Centrality (for directed graphs):** Number of incoming edges to a vertex.
     - **Out-Degree Centrality (for directed graphs):** Number of outgoing edges from a vertex.

2. **Betweenness Centrality:**
   - **Definition:** Measures the number of times a vertex acts as a bridge along the shortest path between two other vertices.
   - **Use:** Identifies vertices that are critical for information flow in the network.

3. **Closeness Centrality:**
   - **Definition:** The reciprocal of the sum of the shortest path distances from a vertex to all other vertices.
   - **Use:** Indicates how close a vertex is to all other vertices in the graph, representing efficiency in spreading information.

4. **Eigenvector Centrality:**
   - **Definition:** Measures the influence of a vertex in a network based on the influence of its neighbors.
   - **Use:** Identifies vertices with high influence that are connected to other highly influential vertices.

5. **PageRank:**
   - **Definition:** An algorithm originally used by Google to rank web pages, measuring the importance of vertices based on the structure of incoming links.
   - **Use:** Identifies important vertices based on the quality and quantity of connections.

6. **Clustering Coefficient:**
   - **Definition:** Measures the degree to which vertices in a graph tend to cluster together.
   - **Use:** Indicates the presence of tightly knit groups or communities within the network.

7. **Community Detection:**
   - **Definition:** Identifies groups of vertices that are more densely connected to each other than to the rest of the graph.
   - **Use:** Helps to understand the modular structure of the network and identify functional units.

8. **Shortest Path Analysis:**
   - **Definition:** Determines the shortest path between pairs of vertices.
   - **Use:** Useful for analyzing the efficiency of routes and connections in the network.

9. **Graph Density:**
   - **Definition:** The ratio of the number of edges to the number of possible edges.
   - **Use:** Indicates how densely connected the graph is.

10. **Assortativity:**
    - **Definition:** Measures the tendency of vertices to connect to other vertices with similar properties (e.g., degree).
    - **Use:** Indicates whether high-degree vertices tend to connect to other high-degree vertices (positive assortativity) or low-degree vertices (negative assortativity).

11. **Network Motifs:**
    - **Definition:** Small, recurring subgraph patterns.
    - **Use:** Identifies basic building blocks of complex networks, which can reveal structural and functional properties.

12. **Graph Laplacian and Spectral Analysis:**
    - **Definition:** Uses eigenvalues and eigenvectors of the graph Laplacian matrix.
    - **Use:** Analyzes properties like connectivity, graph partitioning, and clustering.
