import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import numpy as np

fin = open('torchnet_test_loss.log')
finq = open('Q.log')

ar = []
for i in fin:
    ar.append(i[:-1])
q = []
for i in finq:
	q.append(i[:-1])

ar = [float(ar[i]) for i in range(len(ar)) if i%5 == 4 ]
print(ar)
##baseline VS last episode

t = range(0, len(ar))

plt.figure(1)
t = np.array(t)
q = np.array(q)
ar = np.array(ar)
plt.subplot(121)
plt.plot(t, ar)
plt.title('Test acc')

plt.subplot(122)
plt.plot(t, q)
plt.title('Q value')

#plt.title('')
#plt.ylabel('Accuracy(%)')
#plt.xlabel('Epoch')
#plt.plot(t, ar, label='qan')
#plt.legend(loc='lower right')

plt.savefig('acc.pdf')


