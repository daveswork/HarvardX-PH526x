import random

random.seed(1)

def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    moving_avg = []
    for i in range(0, n):
        moving_avg.append((x[i] + x[i+1] + x[i+2])/3)
    return moving_avg
    # To complete the function,
    # return a list of the mean of values from i to i+width for all values i from 0 to n-1.

x=[0,10,5,3,1,5]
#print(moving_window_average(x, 1))

R = 1000

x = [random.uniform(0,1) for x in range(R)]

y = [x] + [moving_window_average(x,i) for i in range(1,10)]

ranges = []
for i in range(10):
    test = sorted(y[i])
    ranges.append(test[len(test)-1] - test[0])
    test = []
print(ranges)
