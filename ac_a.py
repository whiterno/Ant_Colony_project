from random import random, choices
from matplotlib import pyplot as plt, animation
import networkx as nx

plt.rcParams["figure.figsize"] = [6, 6]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()


def print_matrix(matrix):
    for x in matrix:
        for o in x:
            print(str(o).ljust(7), end=' ')
        print()


supplement_to_delta = 55
alfa = float(open("alpha.txt", "r").read())  # константа, определяемая зависимость выбора от феромона
beta = float(open("beta.txt", "r").read())  # константа, определяемая зависимость выбора от пути
surplus_const = 25  # константа при расчете близости
evaporation_coefficient = float(open("evap_coef.txt", "r").read())  # коэффициент испарения
initial_pheromone = 0.2  # начальное кол-во феромона

f = open("ga_data.txt", "r")
data = f
coordinates = []  # общий список точек
for c in data:
    coordinates.append(tuple([int(num) for num in c.split()]))  # создаем список кортежей

points = len(coordinates)  # количество точек

matrix_of_distances = [[0] * points for _ in range(points)]  # матрица расстояний
for i in range(points):
    for j in range(points):
        x1 = coordinates[i][0]
        y1 = coordinates[i][1]
        x2 = coordinates[j][0]
        y2 = coordinates[j][1]
        matrix_of_distances[i][j] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

delta_pheromone_matrix = [[0] * points for _ in range(points)]

pheromone_matrix = [[0] * points for _ in range(points)]
for f in range(points):
    for r in range(points):
        if f != r:
            pheromone_matrix[f][r] = initial_pheromone


def surch_denominator(visit, start):
    sm = 0

    for u in range(points):

        if coordinates[u] in visit or u == start:
            continue

        sm += pheromone_matrix[start][u] ** alfa * (
                surplus_const / matrix_of_distances[start][u]) ** beta
    return sm


def add_to_delta_pheromone(ways, length):
    for u in range(points):
        if u != points - 1:
            i1, j1 = sorted(ways[u:u + 2])
        else:
            i1, j1 = sorted([ways[0], ways[-1]])

        delta_pheromone_matrix[i1][j1] += supplement_to_delta / length


def add_to_pheromone():
    for q in range(points):
        for r in range(q+1, points):
            pheromone_matrix[q][r] *= evaporation_coefficient
            pheromone_matrix[q][r] += delta_pheromone_matrix[q][r]
            pheromone_matrix[r][q] = pheromone_matrix[q][r]

G = nx.Graph()
W = nx.Graph()
G.add_nodes_from([i for i in range(points)])
W.add_nodes_from([i for i in range(points)])
pos = {}
for i in range(points):
    pos[i] = coordinates[i]
weights = []




def change_weights(matrix):
    global weights
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            weights.append(tuple([i, j, matrix[i][j]]))


change_weights(pheromone_matrix)
G.add_weighted_edges_from(weights)
nx.draw(G, pos, with_labels=True)

cnt = 1
length = []


def animate(frame):
    global delta_pheromone_matrix, start_point, cnt
    fig.clear()
    W.clear_edges()
    start_point = cnt % points
    visited = [coordinates[start_point]]
    total_length = 0
    way = [start_point]  # маршрут муравья
    for i in range(points):  # муравей переходит в следующую точку, ищем новые вероятности

        if i == points - 1:
            total_length += matrix_of_distances[start_point][way[0]]
            continue

        probabilities = []  # Список вероятностей

        denominator_of_probability = surch_denominator(visited, start_point)  # Знаменатель вероятности
        for k in range(points):
            if k == start_point or coordinates[k] in visited:  # в эту же точку или в которой уже побывал
                probabilities.append((0, k))
                continue

            probabilities.append(((pheromone_matrix[start_point][k] ** alfa * (
                    surplus_const / matrix_of_distances[start_point][k]) ** beta) / denominator_of_probability,
                                  k))

        next_point = choices(probabilities, weights=[c[0] for c in probabilities])[0][1]  # следующая точка
        total_length += matrix_of_distances[start_point][next_point]  # Общая длинна траектории муравья
        way.append(next_point)  # записываем путь муравья
        visited.append(coordinates[next_point])  # добавляем предыдущую точку в список пройденных

        start_point = next_point  # новая стартовая точка
    add_to_delta_pheromone(way, total_length)

    edges = []
    for i in range(len(way) - 1):
        edges.append((way[i], way[i + 1]))
    edges.append((way[-1], way[0]))
    W.add_edges_from(edges)

    if cnt % (points * 2) == 0:
        add_to_pheromone()
        delta_pheromone_matrix = [[0] * points for _ in range(points)]
        G.clear_edges()
        change_weights(pheromone_matrix)
        G.add_weighted_edges_from(weights)

    weigh = [G[u][v]['weight'] * 4 for u, v in G.edges()]
    #edge_labels = {(u, v):round(d['weight'], 2)for u,v,d in G.edges(data=True)}
    #nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw_networkx_edges(G, pos, edge_color='#DEB887', width=weigh)
    nx.draw_networkx(W, pos, with_labels=True)
    cnt += 1
    length.append(total_length)
    print(cnt)


def ant_algoritm(num):
    for _ in range(points):  # один маршрут
        start_point = num
        visited = [coordinates[start_point]]
        total_length = 0
        way = [start_point]  # маршрут муравья
        for i in range(points):  # муравей переходит в следующую точку

            if i == points - 1:
                total_length += matrix_of_distances[start_point][way[0]]
                continue

            probabilities = []  # Список вероятностей

            denominator_of_probability = surch_denominator(visited, start_point)  # Знаменатель вероятности
            for k in range(points):
                if k == start_point or coordinates[k] in visited:  # в эту же точку или в которой уже побывал
                    probabilities.append((0, k))
                    continue

                probabilities.append(((pheromone_matrix[start_point][k] ** alfa * (
                        surplus_const / matrix_of_distances[start_point][k]) ** beta) / denominator_of_probability, k))

            next_point = choices(probabilities, weights=[c[0] for c in probabilities])[0][1]  # следующая точка
            total_length += matrix_of_distances[start_point][next_point]  # Общая длинна траектории муравья
            way.append(next_point)  # записываем путь муравья
            visited.append(coordinates[next_point])  # добавляем предыдущую точку в список пройденных

            start_point = next_point  # новая стартовая точка

    return [way, total_length]


ani = animation.FuncAnimation(fig, animate, frames=100 * points, interval=int(open("interval.txt", "r").read()),
                              repeat=False)

plt.show()

data = open("ga_data.txt", "w")
data.write(str(ant_algoritm(1)[1]))
data.close()
data = open('length.txt', 'w')
for i in range(len(length)):
    length[i] = str(length[i])
data.write(" ".join(length))
