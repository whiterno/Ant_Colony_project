from itertools import permutations
from matplotlib import pyplot as plt, animation
import networkx as nx
import time

plt.rcParams["figure.figsize"] = [6, 6]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()


f = open("ga_data.txt", "r")
data = f
coordinates = []  # общий список точек
for c in data:
    coordinates.append(tuple([int(num) for num in c.split()]))  # создаем список кортежей
n = len(coordinates)  # количество точек

G = nx.DiGraph()
G.add_nodes_from([i for i in range(n)])
pos = {}
for i in range(n):
    pos[i] = coordinates[i]


points = len(coordinates)  # количество точек

start = time.time()

matrix_of_distances = [[0] * points for _ in range(points)]  # матрица расстояний
for i in range(points):
    for j in range(points):
        x1 = coordinates[i][0]
        y1 = coordinates[i][1]
        x2 = coordinates[j][0]
        y2 = coordinates[j][1]
        matrix_of_distances[i][j] = round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2), 2)  # УБРАТЬ ОКРУГЛЕНИЕ !!!

all_ways = list(permutations([i for i in range(points)]))

minimum = 10**101

for way in all_ways:
    start_point = way[0]
    total_length = 0
    for i in range(1, points):

        next_point = way[i]
        total_length += matrix_of_distances[start_point][next_point]

        start_point = next_point
    total_length += matrix_of_distances[way[-1]][way[0]]

    if total_length < minimum:
        new_way = way
        minimum = total_length

end = time.time()

f = open("ga_data.txt", "w")
f.write(str(minimum))
f.close()

t = open("time.txt", "w")
t.write(str(end - start))
t.close()

edges = []
for i in range(len(new_way) - 1):
    edges.append((new_way[i], new_way[i + 1]))
edges.append((new_way[-1], new_way[0]))

nx.draw(G, pos, with_labels=True)
i = 0


def animate(frame):
    global i, pos
    fig.clear()
    G.add_edge(*edges[i])
    nx.draw(G, pos, with_labels=True)
    i += 1


ani = animation.FuncAnimation(fig, animate, frames=n - 1, interval=1000, repeat=False)

plt.show()


