import turtle
import math

def star(n, s = 100):
    """
    画出一个n角星
    """
    a = (n - 2) * 180 / n #n边形的内角度数
    b = (180 - a) * 2 # n边形转向角度
    if n % 2 == 1:
        for i in range(n):
            turtle.fd(s)
            turtle.rt(b)
    else:
        for j in range(2):
            for i in range(n//2):
                turtle.fd(s)
                turtle.rt(b)
            turtle.up()
            c = (180 - a) / 2
            d = s / 2 / math.cos(c / 180 * math.pi)
            turtle.lt(c)
            turtle.fd(d)
            turtle.rt(c + (180 - a))
            turtle.down()

          


if __name__== '__main__':
    star(5)
    turtle.mainloop()