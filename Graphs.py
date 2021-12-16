class Graphs:
    def __init__(self):
        self.adj_list = {}

    def print_graphs(self):
        for vertex in self.adj_list:
            print(vertex, ": ", self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        try:
            if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
                return True
        except ValueError:
            pass
        return False


mygraph = Graphs()

mygraph.add_vertex('A')
mygraph.add_vertex('B')
mygraph.add_vertex('C')
mygraph.add_vertex('D')

mygraph.add_edge('A', 'B')
mygraph.add_edge('B', 'C')
mygraph.add_edge('C', 'A')

mygraph.remove_edge('D', 'A')

mygraph.print_graphs()
