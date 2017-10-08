import math
import random

def rand():
    return random.uniform(-1, 1)

def distance(x,y):
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2  )

def in_circle(x, origin = [0]*2):
   # Define your function here!
   if distance(x, origin) < 1:
       return True
   else:
       return False
R = 10000
x = []
inside = []
for i in range(R):
    point = [rand(), rand()]
    x.append(point)
    if in_circle(x[i]):
        inside.append(True)
    else:
        inside.append(False)
print(inside.count(True)/R)
