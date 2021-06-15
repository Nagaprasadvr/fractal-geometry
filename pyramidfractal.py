import math
from math import *
import random
from random import randint
import plotly
import plotly.express as px


n = 10000
x = [0.0] * n
y = [0.0] * n
z = [0.0] * n
m = random.randint(1, 6)
j = random.randint(1, 6)
c = random.randint(1, 6)
p1 = [0, 0, 0]
p2 = [2.5, 5.33012, 0]
p3 = [5, 0, 0]
p4 = [2.5, 2.6656, 8.0]

x.insert(0, p1[0])
y.insert(0, p1[1])
z.insert(0, p1[2])
x.insert(1, p2[0])
y.insert(1, p2[1])
z.insert(1, p2[2])
x.insert(2, p3[0])
y.insert(2, p3[1])
z.insert(2, p3[2])
x.insert(3, m)
y.insert(3, j)
z.insert(3, c)
for i in range(3, n + 2):
    a = random.randint(1, 8)
    if a == 1 or a == 2:
        k = (x[i] + p1[0]) / 2
        l = (y[i] + p1[1]) / 2
        v = (z[i] + p1[2]) / 2
        x.insert((i + 1), k)
        y.insert((i + 1), l)
        z.insert((i + 1), v)


    elif a == 3 or a == 4:
        c = (x[i] + p2[0]) / 2
        d = (y[i] + p2[1]) / 2
        v = (z[i] + p2[2]) / 2
        x.insert((i + 1), c)
        y.insert((i + 1), d)
        z.insert((i + 1), v)
    elif a == 5 or a == 6:
        e = (x[i] + p3[0]) / 2
        f = (y[i] + p3[1]) / 2
        v = (z[i] + p3[2]) / 2
        x.insert((i + 1), e)
        y.insert((i + 1), f)
        z.insert((i + 1), v)
    if a == 7 or a == 8:
        k = (x[i] + p4[0]) / 2
        l = (y[i] + p4[1]) / 2
        v = (z[i] + p4[2]) / 2
        x.insert((i + 1), k)
        y.insert((i + 1), l)
        z.insert((i + 1), v)
t = []
for s in range(0, len(x)):
   t.append(s)



fig = px.scatter_3d(x = x, y = y,z = z ,title = "fractal", height=700)
fig.update_traces(marker_size=1)
fig.write_html("pyramid.html")
print("done")


