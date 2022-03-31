# PREDLOŽAK ZA SIMULACIJE GIBANJA
#
# Ovaj kod namijenjen je kao predložak za simulacije u kojima
# se radi numeričke izračune za gibanje tijela.
# Prilagodite ga ovisno o tome što se traži, a za primjer korištenja
# pogledajte "ispaljivanje kuglice.ipynb"

from matplotlib.pyplot import *

#parametri:
m = 1
g = 9.81

# vremenski korak (delta t) i trajanje (t konačno):
dt = 0.01
t_k = 10

# početne vrijednosti veličina koje računamo:
t = 0
x = 0
y = 0
vx = 0
vy = 0

# liste za izradu grafova
vremena = [t]
pomaci_x = [x]
pomaci_y = [y]

while t < t_k:
    # sile u oba smjera, ovaj dio prilagodite modelu:
    fx = 0
    fy = -m*g
    # izračun pomaka za 2D gibanje:
    ax = fx/m
    ay = fy/m
    vx = vx + ax*dt
    vy = vy + ay*dt
    x = x + vx*dt
    y = y + vy*dt
    t = t + dt
    vremena.append(t)
    pomaci_x.append(x)
    pomaci_y.append(y)

#crtanje grafa
title('Ovdje dođe naslov vašeg grafa')
xlabel('oznaka i mjerna jedinica za x os')
ylabel('oznaka i mjerna jedinica za y os')
plot(vremena,pomaci_x,'r.')
show()