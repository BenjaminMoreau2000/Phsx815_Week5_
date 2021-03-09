#Ben Moreau

#Integrate e^x from 0 to 1, which is e-1

from math import  *

print("The analytical integral of e^x from -1 to 1 is:", (exp(1)-exp(-1)))

print("Input the max number of rectangles")

N=int(input())

#Rectangles
def eee(x):
    return exp(x)


Areas=[]
AreasE=[]
for i in range(5,N):
    Area=0
    for k in range(i):
        Area+=eee(-1+2/i*k)*2/i
    Areas.append(Area)
    AreasE.append((Area-(exp(1)-exp(-1))))

print("The rectangle integral gives: ",Area)
      
from matplotlib import pyplot as plt

plt.scatter(range(5,len(Areas)+5),AreasE,label="Rectangle Error")

plt.title("Error and difference")
plt.ylabel("Error")
plt.xlabel("Intervals")
plt.legend()

xi=[0,-1/3*sqrt(5-2*sqrt(10/7)),-1/3*sqrt(5+2*sqrt(10/7)),1/3*sqrt(5-2*sqrt(10/7)),1/3*sqrt(5+2*sqrt(10/7))]
wi=[128/225,322/900+13*sqrt(70)/900,322/900-13*sqrt(70)/900]

Area=0
Area+=eee(xi[0])*wi[0]
Area+=eee(xi[1])*wi[1]
Area+=eee(xi[2])*wi[2]
Area+=eee(xi[3])*wi[1]
Area+=eee(xi[4])*wi[2]

print("The gaussian integral gives: ",Area)
print("Acutal - Gauss = ",(exp(1)-exp(-1))-Area,"And the Gauss - Rectangle",Areas[len(Areas)-1]-Area)

print("This means that the Gaussian integral is a very good estimate for the actual integral.")
plt.show()
