from math import sin
from math import cos
from math import radians
from matplotlib import pyplot as plt
v = \
float(input('Masukkan kecepatan awal (m/s) : '))
sudut = \
float(input('Masukkan sudut kemiringan (derajat) : '))
delta_t = \
float(input('Masukkan time step (s) : '))
g,y,x,t = 9.8 , 0.0, 0.0 , 0.0
vx = v*cos(radians(sudut))
vy = v*sin(radians(sudut))
def funx(t) :
    if t == 0 :
        return x
    else :
        xtemp = x + vx * delta_t
        return xtemp

def funy(t) :
    if t == 0 :
        return y
    else :
        ytemp = y + vy*delta_t
        return ytemp

#Main
arrX = []
arrY = []
print("Vx = ","%.3f" % vx,"m/s")
print("")
print("")
print('t\t\t x\t\t\tvy\t\ty')
while y >= 0:
    arrX.append(x)
    arrY.append(y)
    stringt = "%.3f" % t
    stringvy = "%.3f" % vy
    stringx = "%.3f" % x
    stringy = "%.6f" % y
    print(stringt,'\t',stringx,'\t',stringvy, '\t', stringy)
    t = t + delta_t
    x = funx(t)
    vy = vy - g*delta_t
    y = funy(t)

plt.plot(arrX,arrY)
plt.show()