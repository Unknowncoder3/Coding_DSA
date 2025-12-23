"""Dijkstra's shortest-path algorithm (simple implementation).

This module contains a straightforward implementation of Dijkstra's algorithm
that computes the shortest path distances from a source node to all other
nodes in a weighted graph with non-negative edge weights.

Graph representation:
    graph : dict
        A mapping of nodes to adjacency mappings. Example:

        graph = {
            'A': {'B': 5, 'C': 1},
            'B': {'A': 5, 'C': 2, 'D': 1},
            'C': {'A': 1, 'B': 2, 'D': 4},
            'D': {'B': 1, 'C': 4}
        }

Function contract:
    dijkstra(graph, start) -> dict
    Inputs:
        graph: dict where keys are nodes and values are dicts of neighbor->weight
        start: node present in graph to start shortest-path search from
    Output:
        dict mapping each node in graph to its shortest distance from `start`.

Complexity:
    This implementation uses a linear scan to find the next node with the
    smallest tentative distance, giving O(V^2) time complexity. For large or
    sparse graphs prefer a priority queue / heap-based implementation to get
    O((V + E) log V) time.

Notes:
    - Edge weights must be non-negative.
    - Nodes with no reachable path from `start` will have distance sys.maxsize.
"""

import sys


def dijkstra(graph, start):
    """Compute shortest distances from `start` to all nodes using Dijkstra.

    Parameters
    ----------
    graph : dict
        Adjacency mapping {node: {neighbor: weight, ...}, ...}.
    start : hashable
        Starting node (must be a key in `graph`).

    Returns
    -------
    dict
        Mapping of node -> shortest distance (int). Unreachable nodes retain
        the initial sentinel value sys.maxsize.

    Example
    -------
    >>> graph = {
    ...     'A': {'B': 5, 'C': 1},
    ...     'B': {'A': 5, 'C': 2, 'D': 1},
    ...     'C': {'A': 1, 'B': 2, 'D': 4},
    ...     'D': {'B': 1, 'C': 4}
    ... }
    >>> dijkstra(graph, 'A')
    {'A': 0, 'B': 3, 'C': 1, 'D': 4}
    """

    # Initialize distances to a large number (infinity sentinel)
    shortest_distances = {node: sys.maxsize for node in graph}
    shortest_distances[start] = 0
    visited = set()

    # Continue until we've visited every node in the graph
    while len(visited) < len(graph):
        # Pick the unvisited node with the smallest tentative distance.
        # This linear search is the reason this implementation is O(V^2).
        current_node = min(
            (node for node in graph if node not in visited),
            key=lambda node: shortest_distances[node]
        )
        visited.add(current_node)

        # Relaxation step: update distances to neighbors of current_node
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                new_distance = shortest_distances[current_node] + weight
                if new_distance < shortest_distances[neighbor]:
                    shortest_distances[neighbor] = new_distance

    return shortest_distances