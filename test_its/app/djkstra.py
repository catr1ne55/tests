import numpy as np


class Graph:

    def min_distance(self, dist, queue):
        minimum = float("inf")
        min_index = -1
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index

    def get_path(self, pathes, parent, j):
        if parent[j] != -1:
            pathes.append(j)
            return self.get_path(pathes, parent, parent[j])
        pathes.append(j)
        return pathes

    def get_distance(self, dist, parent, destination):
        pathes = []
        path = self.get_path(pathes, parent, destination)
        return dist[destination], path[::-1]

    def dijkstra(self, graph, src, destination):

        row = len(graph)
        col = len(graph[0])
        dist = [float("inf")] * row
        parent = [-1] * row
        src = int(src)
        destination = int(destination)
        dist[src] = 0
        queue = []
        for i in range(row):
            queue.append(i)

        while queue:
            u = self.min_distance(dist, queue)
            queue.remove(u)
            for i in range(col):
                if graph[u][i] and i in queue:
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u
        distance, path = self.get_distance(dist, parent, destination)
        return distance, path
