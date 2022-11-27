import math
import networkx as nx
import matplotlib.pyplot as plt
import time

def get_min(R, U):
    rm = (math.inf, -1, -1)
    for v in U:
        # key=lambda x: x[0] - ищмем минимум по весу реба
        # if (x[1] == v or x[2] == v) - одна из вершин должна быть из множества U
        # (x[1] not in U or x[2] not in U) - одна из вершин не должна быть в множестве U
        rr = min(R, key=lambda x: x[0] if (x[1] == v or x[2] == v) and (x[1] not in U or x[2] not in U) else math.inf)
        if rm[0] > rr[0]:
            rm = rr

    return rm

# список ребер графа (длина, вершина 1, вершина 2)
# первое значение возвращается, если нет минимальных ребер
R = [(math.inf, -1, -1), (12, 2, 3), (10, 1, 6), (8, 5, 8),
     (7, 4, 7), (6, 1, 2), (5, 6, 7), (5, 5, 7), (4, 4, 5),
     (2, 7, 8), (1, 4, 6), (1, 3, 8), (1, 3, 5), (1, 2, 5),
     (1, 2, 4), (1, 1, 4)]

start_time = time.time()
for i in range(10000):
    N = 8     # число вершин в графе
    U = {1}   # множество соединенных вершин, начинаем с первой вершины
    T = []    # список ребер остова

    while len(U) < N:
        r = get_min(R, U)       # ребро с минимальным весом
        if r[0] == math.inf:    # если ребер нет, то остов построен
            break

        T.append(r)             # добавляем ребро в остов
        U.add(r[1])             # добавляем вершины в множество U
        U.add(r[2])

end_time = time.time()
print(end_time-start_time)
print(T)


graph = nx.Graph()
kilometres = set()
for i in T:
    kilometres.add((i[1], i[2], i[0]))
graph.add_weighted_edges_from(kilometres)
nx.draw_circular(graph, node_color='green', node_size=500, with_labels=True)

plt.show()
