import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys

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
ar1 = ar1[0:200]
ar2 = ar2[0:200]
ar3 = ar3[0:200]
##baseline VS last episode

t = range(0, len(ar1))

plt.title('')
plt.ylabel('Accuracy(%)')
plt.xlabel('Epoch')
plt.plot(t, ar1, label='10000')
plt.plot(t, ar2, label='1000')
plt.plot(t, ar3, label='100')
plt.legend(loc='lower right')

plt.savefig('acc.pdf')


