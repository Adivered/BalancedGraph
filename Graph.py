class Graph:

    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
        self.edge_signs = {}

    def DFSUtilPositive(self, temp, v, visited):
        visited[v] = True
        temp.append(v)
        for i in self.adj[v]:
            if (
                not visited[i]
                and (v, i) in self.edge_signs
                and self.edge_signs[(v, i)] == "+"
            ):
                self.DFSUtilPositive(temp, i, visited)
        return temp

    def addEdge(self, v, w, sign):
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.edge_signs[(v, w)] = sign
        ##self.edge_signs[(w, v)] = sign

    def connectedComponents(self):
        visited = [False] * self.V
        cc = []
        for v in range(self.V):
            if not visited[v]:
                temp = []
                if self.DFSUtilPositive(temp, v, visited):
                    cc.append(temp)
        return cc

    def getEdgeSign(self, v, w):
        return self.edge_signs.get((v, w), None)

    def countNegativeEdges(self, connected_components):
        for component1 in connected_components:
            for component2 in connected_components:
                if component1 == component2:
                    continue
                for v in component1:
                    for w in component2:
                        if (
                            w in self.adj[v]
                            and (v, w) in self.edge_signs
                            and self.edge_signs[(v, w)] == "+"
                        ):
                            print(
                                f"Positive edge  ({v} -> {w}): ",
                                self.edge_signs[(v, w)],
                            )
                            return False

        return True


def main():
    graph = Graph(4)
    graph2 = Graph(4)
    graph.addEdge(0, 1, "+")
    graph.addEdge(0, 2, "-")
    graph.addEdge(0, 3, "-")
    graph.addEdge(1, 2, "-")
    graph.addEdge(1, 3, "-")
    graph.addEdge(2, 3, "+")

    graph2.addEdge(0, 1, "-")
    graph2.addEdge(0, 2, "+")
    graph2.addEdge(0, 3, "-")
    graph2.addEdge(1, 2, "+")
    graph2.addEdge(1, 3, "+")
    graph2.addEdge(2, 3, "-")
    cc = graph.connectedComponents()
    cc2 = graph2.connectedComponents()
    print("Following are connected components")
    print(cc)
    msg = "Graph is balanced"
    if not graph.countNegativeEdges(cc):
        msg = "Graph is unbalanced"

    print(msg)
    print("-------------")
    print(cc2)
    if not graph2.countNegativeEdges(cc2):
        msg = "Graph is unbalanced"

    print(msg)


if __name__ == "__main__":
    main()
