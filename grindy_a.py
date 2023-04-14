from matplotlib import pyplot as plt, animation
import networkx as nx

plt.rcParams["figure.figsize"] = [6, 6]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()

f = open("ga_data.txt", "r")
data = f
all_xy = []  # общий список точек
for c in data:
    all_xy.append(tuple([int(num) for num in c.split()]))  # создаем список кортежей
n = len(all_xy)  # количество точек

G = nx.DiGraph()
G.add_nodes_from([i for i in range(n)])
pos = {}
for i in range(n):
    pos[i] = all_xy[i]

start_point = 0  # начальная точка, по умолчанию 0(первая точка)

check_xy = [
    all_xy[0]]  # список точек, через которые уже сделали обход, чтобы из одной точки существовал только один путь
# начальная точка входит в этот список, т.к. мы начинаем из нее

k = 0  # счетчик обходов

sm = 0  # общая длинна пути

while k != n:  # пока не закончатся точки обхода
    k += 1

    if k == n:  # если это последняя точка, то единственный путь - начальная точка
        check_xy.remove(all_xy[0])

    # координаты начальной точки
    x0 = all_xy[start_point][0]
    y0 = all_xy[start_point][1]

    mn = 10 ** 20  # находим минимальную длину
    for i in range(n):
        # координаты точки по обходу
        x1 = all_xy[(start_point + i) % n][0]  # остаток от n, если начальная точка не в начале списка
        y1 = all_xy[(start_point + i) % n][1]
        if (x1, y1) not in check_xy:  # обходим только нетронутые точки
            if (x1 - x0) ** 2 + (y1 - y0) ** 2 < mn:  # проверяем расстояние
                mn = (x1 - x0) ** 2 + (y1 - y0) ** 2  # новый макс
                mn_index = (start_point + i) % n  # индекс точки, длинна которой с начальной - максимальная
    check_xy.append(all_xy[mn_index])  # добавляем в список точку в которую мы перешли
    start_point = mn_index  # новая начальная точка
    sm += mn ** (1 / 2)

check_xy = [check_xy[-1]] + check_xy

f = open("ga_data.txt", "w")
f.write(str(sm))


def get_key(d, value):
    for key, val in d.items():
        if val == value:
            return key


nodes_order = [get_key(pos, val) for val in check_xy]
edges = []
for i in range(len(nodes_order) - 1):
    edges.append((nodes_order[i], nodes_order[i + 1]))

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