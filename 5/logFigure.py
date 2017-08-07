#test
#encoding: utf-8
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import logRegress as l

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X,y = l.loadData("./data/（3维）titanic.mat");
w  = l.grad(X,y);

xs = X[:,1];
ys = X[:,2];
zs = X[:,3];

x1 = [0.1:0.1:1];
x2 = [0.1:0.1:1];
x1 = (mat(x1)).T;
x2= (mat(x2)).T;
x = column_stack(ones(len(x1),1),x1);
x =  column_stack(x1,x2);

z = (mat(x)).*w
#print xs[0,0];

#for i in range(len(xs)):
	

'''xs = [1,2,3,4];
print xs[1];
ys = [3,4,6,3];
zs = [3,6,8,4];'''

ax.scatter(xs.getA(), ys.getA(), zs.getA());
ax.set_xlabel('X1 Label')
ax.set_ylabel('X2 Label')
ax.set_zlabel('X3 Label')

plt.show()

'''n = 100

# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()'''
