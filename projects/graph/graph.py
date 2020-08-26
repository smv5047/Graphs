"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    # TODO

    def __init__(self):
        self.vertices = {
            # 1: {2},
            # 2: {3, 4},
            # 7: {1, 6}
        }
        # space O(v) + O(e)

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # create the new key with the vertex id and set the value to an empty set
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
        # O(1)

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # find vertex V1 in our vertices, add V2 to the set of edges
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        # O(1)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
        # O(1)

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # crete an empty queue and enqueue the starting vertex
        # create an empty set to track visited verticies

        # while the queu is not empty

        # get current vertex (dequeu from queue)
        # check if the current vertex has not been visited
        # print the current vertex
        # mark current vertex as visited (so we don't get stuck)
        # add the current vertex to a visited_set

        # queue up all the current vertecies neighbors(so we can visit them next)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # crete an empty stack and enqueue the starting vertex
        # create an empty set to track visited verticies

        # while the stack is not empty

        # get current vertex (pop from stack)
        # check if the current vertex has not been visited
        # print the current vertex
        # mark current vertex as visited (so we don't get stuck)
        # add the current vertex to a visited_set

        # push up all the current vertecies neighbors(so we can visit them next)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # crete an empty queue and enqueue the PATH TO starting vertex
        queue = Queue()
        visited_verticies = set()
        # create an empty set to track visited verticies
        queue.enqueue({
            'current_vertex': starting_vertex,
            'path': [starting_vertex]
        })

        # while the queu is not empty
        while queue.size() > 0:
            # get current vertex path(dequeu from queue)
            current_obj = queue.dequeue()
            current_path = current_obj['path']
            current_vertex = current_obj['current_vertex']
        # check if the current vertex has not been visited
            if current_vertex not in visited_verticies:
                # CHECK IF THE CURRENT VERTEX IS DESTINATION
                # IF IT IS, STOP AND RETURN
                if current_vertex == destination_vertex:
                    return current_path

        # mark current vertex as visited (so we don't get stuck)
                visited_verticies.add(current_vertex)
        # add the current vertex to a visited_set

                for neighbor_vertex in self.get_neighbors(current_vertex):
                    # queue up NEw pats with each neighbor:
                    # take current path
                    # append the beighbor to is
                    # quue up NEW path
                    # Example [1,2] then [1,2,3], [1,2,4] and [1,2] gets removed. So we keep replaceing the paths
                    new_path = list(current_path)
                    new_path.append(neighbor_vertex)

                    queue.enqueue({
                        'current_vertex': neighbor_vertex,
                        'path': new_path
                    })

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        """
           Return a list containing the shortest path from
           starting_vertex to destination_vertex in
           breath-first order.
           """
        # crete an empty queue and enqueue the PATH TO starting vertex
        stack = Stack()
        visited_verticies = set()
        # create an empty set to track visited verticies
        stack.push: ({
            'current_vertex': starting_vertex,
            'path': [starting_vertex]
        })

        # while the queu is not empty
        while stack.size() > 0:
            # get current vertex path(dequeu from queue)
            current_obj = stack.pop()
            current_path = current_obj['path']
            current_vertex = current_obj['current_vertex']
        # check if the current vertex has not been visited
            if current_vertex not in visited_verticies:
                # CHECK IF THE CURRENT VERTEX IS DESTINATION
                # IF IT IS, STOP AND RETURN
                if current_vertex == destination_vertex:
                    return current_path

        # mark current vertex as visited (so we don't get stuck)
                visited_verticies.add(current_vertex)
        # add the current vertex to a visited_set

                for neighbor_vertex in self.get_neighbors(current_vertex):
                    # queue up NEw pats with each neighbor:
                    # take current path
                    # append the beighbor to is
                    # quue up NEW path
                    # Example [1,2] then [1,2,3], [1,2,4] and [1,2] gets removed. So we keep replaceing the paths
                    new_path = list(current_path)
                    new_path.append(neighbor_vertex)

                    # stack.enqueue({
                    #     'current_vertex': neighbor_vertex,
                    #     'path': new_path
                    # })

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
