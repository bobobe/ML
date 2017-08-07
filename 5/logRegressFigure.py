 #a test
 # encoding: utf-8
'''
==============
3D scatterplot
==============

Demonstration of a basic scatterplot in 3D.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import logRegress as l

X ,y = l.loadData('./data/（3维）titanic.mat');
w = l.grad(X,y);

w = w.getA();



x1 = X[:,1].getA();
x2 = X[:,2].getA();
x3 = X[:,3].getA();

l1 = np.arange(-3,3,0.5);
l2 = np.arange(-3,3,0.5);
l3 = (-w[0]-w[1]*l1-w[2]*l2)/w[3];

print l1,l2,l3
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x1,x2,x3,c='red');
ax.plot(l1,l2,l3,c = "green");
#ax.plot([1,2,3],[3,4,1],[8,4,1],'--')


plt.show()
