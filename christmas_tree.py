import turtle as tt
import random
import time

n = 80.0

tt.speed("fastest")
tt.screensize(bg='seashell')
tt.left(90)
tt.forward(3*n)
tt.color("orange", "yellow")
tt.begin_fill()
tt.left(126)

for i in range(5):
    tt.forward(n/5)
    tt.right(144)
    tt.forward(n/5)
    tt.left(72)
tt.end_fill()
tt.right(126)

tt.color("dark green")
tt.backward(n*4.8)


def tree(d, s):
    if d <= 0:
        return
    tt.forward(s)
    tree(d - 1, s * .8)
    tt.right(120)
    tree(d - 3, s * .5)
    tt.right(120)
    tree(d - 3, s * .5)
    tt.right(120)
    tt.backward(s)


tree(15, n)
tt.backward(n/2)

for i in range(200):
    a = 200 - 400 * random.random()
    b = 10 - 20 * random.random()
    tt.up()
    tt.forward(b)
    tt.left(90)
    tt.forward(a)
    tt.down()
    if random.randint(0 ,1) == 0:
        tt.color('tomato')
    else:
        tt.color('wheat')
    tt.circle(2)
    tt.up()
    tt.backward(a)
    tt.right(90)
    tt.backward(b)

time.sleep(60)
