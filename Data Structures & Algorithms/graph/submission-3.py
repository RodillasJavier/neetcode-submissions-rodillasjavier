from collections import deque


class Graph:
    def __init__(self):
        """
        init an empty undirected graph
        """
        self.adj_list = {}

    def addEdge(self, src: int, dst: int) -> None:
        """
        add an edge from src to dst if it DNE

        if either src or dst exist, add them to the graph
        """
        if src not in self.adj_list:
            self.adj_list[src] = set()
        if dst not in self.adj_list:
            self.adj_list[dst] = set()

        self.adj_list[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        """
        remove the edge from src to dst if it exists

        return True iff the edge was removed else False
        """
        if src not in self.adj_list:
            return False
        if dst not in self.adj_list:
            return False

        self.adj_list[src].discard(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        """
        return whether there is a path from src to dst
        """
        queue = deque([src])
        visited = set([src])

        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()

                if current == dst:
                    return True

                for neighbor in self.adj_list[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        return False


# time complexity: O(V + E)
# space complexity: O(V)
