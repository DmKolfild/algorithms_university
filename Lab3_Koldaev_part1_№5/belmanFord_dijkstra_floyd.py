import networkx as nx
import matplotlib.pyplot as plt
import time

# Неориентированные графы
G = nx.Graph()
e = [('1', '2', 6), ('1', '4', 1), ('1', '6', 10),
     ('2', '4', 1), ('2', '5', 1), ('2', '3', 12),
     ('3', '5', 1), ('3', '8', 1), ('4', '6', 1),
     ('4', '7', 7), ('4', '5', 4), ('5', '8', 8),
     ('5', '7', 5), ('5', '8', 8), ('6', '7', 1),
     ('7', '8', 2)]
e1 = [('1', '2', 6), ('2', '3', 12), ('3', '4', 1),('4', '5', 7),
      ('5', '6', 4), ('6', '7', 8), ('7', '8', 2)]
e2 = [('1', '2', 6), ('1', '3', 12), ('2', '3', 4), ('1', '4', 7),
      ('2', '4', 4), ('3', '4', 8)]

G.add_weighted_edges_from(e)  # указать исследуемый граф e/e1/e2

start = '7'    # указать начальную и конечную вершину для поиска пути
end = '1'

# алгоритм Беллмана - Форда
time_start = time.time()
for i in range(1000):
     a = nx.bellman_ford_path(G, start, end)
     b = nx.bellman_ford_path_length(G, start, end)
end_time = time.time()
print(end_time-time_start)
print(nx.bellman_ford_path(G, start, end))
print(nx.bellman_ford_path_length(G, start, end))

# алгоритм Флойда
time_start = time.time()
for i in range(1000):
     fw, _ = nx.floyd_warshall_predecessor_and_distance(G, weight='weight')  # нашли путь
     fw2 = nx.floyd_warshall(G, weight='weight')  # нашли длину пути
end_time = time.time()
print(end_time-time_start)
print(nx.reconstruct_path(start, end, fw))
print(fw2[start][end])

# алгоритм Дейкстры
time_start = time.time()
for i in range(1000):
     a = nx.dijkstra_path(G, start, end)
     b = nx.dijkstra_path_length(G, start, end)
end_time = time.time()
print(end_time-time_start)
print(nx.dijkstra_path(G, start, end))
print(nx.dijkstra_path_length(G,  start, end))

plt.figure(1)
nx.draw_circular(G, node_color='green', node_size=500, with_labels=True)



# Ориентированные графы
G1 = nx.DiGraph()
e = [('1', '2', 3), ('1', '3', 8), ('1', '4', 4),
     ('2', '3', 4), ('2', '6', 6), ('3', '6', 6),
     ('3', '5', 7), ('3', '7', 8), ('4', '3', 10),
     ('4', '5', 9), ('5', '7', 3), ('6', '7', 4)]
e1 = [('1', '2', 6), ('2', '3', 12), ('3', '4', 1),('4', '5', 7),
      ('5', '6', 4), ('6', '7', 8), ('7', '8', 2)]
e2 = [('1', '2', 6), ('2', '1', 6), ('1', '3', 12), ('3', '1', 12),
      ('2', '3', 4), ('1', '4', 7), ('2', '4', 4), ('3', '4', 8)]
G1.add_weighted_edges_from(e)  # указать исследуемый граф e/e1/e2

start = '7'    # указать начальную и конечную вершину для поиска пути
end = '7'

# алгоритм Беллмана - Форда
time_start = time.time()
for i in range(1000):
     a = nx.bellman_ford_path(G1, start, end)
     b = nx.bellman_ford_path_length(G1, start, end)
end_time = time.time()
print(end_time-time_start)
print(nx.bellman_ford_path(G1, start, end))
print(nx.bellman_ford_path_length(G1, start, end))

plt.figure(2)
nx.draw_circular(G1, node_color='red', node_size=500, with_labels=True)

plt.show()
