from math import sin
from math import cos
from math import radians
from math import sqrt
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')
plt.style.use('ggplot')

v = 50 #inisialisasi
sudut = 35
delta_t = 0.01
print('Kecepatan awal : ', v, ' m/s')
print('Sudut tembak : ', sudut, ' derajat')
print('Time step : ', delta_t, ' s')
g,y,x,t = 9.8 , 0.0, 0.0 , 0.0
D = 0.0013
m = 0.15
print('Massa objek : ', m,' kg')
vx = v*cos(radians(sudut))
vy = v*sin(radians(sudut))
print('vx : ', vx, ' m/s')
print('vy : ', vy, ' m/s')
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

arrX = []
arrY = []
print("Vx = ","%.3f" % vx,"m/s")
print("")
print('')
print("")
print("Tanpa memperhitungkan hambatan udara")
print('t\t\t x\t\t\tvy\t\t\ty')
while y >= 0:
    arrX.append(x) #menyimpan plotingan x,kan setiap x disimpan
    arrY.append(y)
    stringt = "%.2f" % t
    stringvy = "%.3f" % vy
    stringx = "%.3f" % x
    stringy = "%.6f" % y
    print(stringt,'\t',stringx,'\t',stringvy, '\t', stringy)
    t = t + delta_t #untuk melanjutkan ke iterasi berikutnya
    x = funx(t) #update nilai x
    vy = vy - g*delta_t
    y = funy(t)

plt.plot(arrX,arrY)
arrX2 = [] #menyimpan x dg hambatan
arrY2 = []

v = 50
y,x,t = 0.0,0.0,0.0
vx = v*cos(radians(sudut))
vy = v*sin(radians(sudut))
v = sqrt(vx*vx+vy*vy)
ax = -(D/m)*v*vx
ay = -g-(D/m)*v*vy
print("\n\n")
print("Dengan mempertimbangkan hambatan udara")
print('t\t\t x\t\t\tvy\t\t\ty')
while y >=0 :
    arrX2.append(x)
    arrY2.append(y)
    stringt = "%.2f" % t
    stringvy = "%.3f" % vy
    stringx = "%.3f" % x
    stringy = "%.6f" % y
    print(stringt, '\t', stringx, '\t', stringvy, '\t', stringy)
    t = t + delta_t
    vy = vy+ay*delta_t
    vx = vx+ax*delta_t
    v = sqrt(vx * vx + vy * vy)
    ax = -(D/m)*v*vx
    ay = -g-(D/m)*v*vy
    x = funx(t)
    y = funy(t)

print('Jika hambatan udara tidak diperhitungkan, posisi benda berada di : (',arrX[len(arrX)-1],',0)')
print('Jika hambatan diperhitungkan, posisi benda berada di : (',arrX2[len(arrX2)-1],',0)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot gerak peluru')

plt.plot(arrX2,arrY2)
plt.legend(['Tanpa Hambatan Udara','Dengan hambatan udara'])
plt.grid(True)
plt.show()