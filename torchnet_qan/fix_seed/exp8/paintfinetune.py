import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import numpy as np

fin = open('torchnet_test_loss.log')
finq = open('Q.log')

ar = []
localnum = 0
localar = []
for i in fin:
	localnum += 1
	localar.append(i[:-1])
	if localnum == 6:
		ar.append(localar[:-1])
		localar = []
		localnum = 0
q = []
for i in finq:
	q.append(i[:-1])


q = [ q[i] for i in range(len(q)) if i%2 == 1 ]
ar = [ ar[i] for i in range(len(ar)) if i%2 == 1 ]
ave_acc = []
for i in range(len(ar)):
	ar[i] = [float(x) for x in ar[i]]
	ave_acc.append(np.mean(ar[i]))
print(ave_acc)
print(q)

assert(len(ave_acc) == len(q))
t = range(0, len(ave_acc))

plt.figure(1)
t = np.array(t)
q = np.array(q)
ar = np.array(ave_acc)
plt.subplot(121)
plt.plot(t, ar)
plt.title('Ave acc')

plt.subplot(122)
plt.plot(t, q)
plt.title('Q value')

#plt.title('')
#plt.ylabel('Accuracy(%)')
#plt.xlabel('Epoch')
#plt.plot(t, ar, label='qan')
#plt.legend(loc='lower right')

plt.show()
plt.savefig('acc.pdf')


