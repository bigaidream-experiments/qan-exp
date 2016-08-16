import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import numpy as np

fin1 = open('10000.log')
fin2 = open('1000.log')
fin3 = open('100.log')

ar1 = []
for i in fin1:
    ar1.append(i[:-1])

ar2 = []
for i in fin2:
	ar2.append(i[:-1])

ar3 = []
for i in fin3:
	ar3.append(i[:-1])
ar1 = np.array(ar1[0:200])
ar2 = np.array(ar2[0:200])
ar3 = np.array(ar3[0:200])
##baseline VS last episode

t = np.array(range(0, len(ar1)))

plt.figure(1)

# linear
plt.subplot(221)
plt.plot(t, ar1)
plt.title('10000')
#plt.grid(True)

# log
plt.subplot(222)
plt.plot(t, ar2)
plt.title('1000')
#plt.grid(True)


# symmetric log
plt.subplot(223)
plt.plot(t, ar3)
plt.title('100')
#plt.grid(True)


plt.savefig('acc.pdf')


