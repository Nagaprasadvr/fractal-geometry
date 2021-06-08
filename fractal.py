import math
from math import *
import random
from random import randint
import plotly
import plotly.express as px

n = 10000
x = [0.0] * n
y = [0.0] * n
m = random.randint(1, 6)
j = random.randint(1, 6)
p1 = [0, 0]
p2 = [2.5, 4.33012]
p3 = [5, 0]

x.insert(0, p1[0])
y.insert(0, p1[1])
x.insert(1, p2[0])
y.insert(1, p2[1])
x.insert(2, p3[0])
y.insert(2, p3[1])
x.insert(3, m)
y.insert(3, j)
for i in range(3, n + 2):
    a = random.randint(1, 6)
    if a == 1 or a == 2:
        k = (x[i] + p1[0]) / 2
        l = (y[i] + p1[1]) / 2
        x.insert((i + 1), k)
        y.insert((i + 1), l)

    elif a == 3 or a == 4:
        c = (x[i] + p2[0]) / 2
        d = (y[i] + p2[1]) / 2
        x.insert((i + 1), c)
        y.insert((i + 1), d)
    elif a == 5 or a == 6:
        e = (x[i] + p3[0]) / 2
        f = (y[i] + p3[1]) / 2
        x.insert((i + 1), e)
        y.insert((i + 1), f)

fig = px.scatter(x=x, y=y, title="fractal", height=700,animation_frame=x)
fig.update_traces(marker_size=3)
fig.write_html("fractal.html")
print("done")


