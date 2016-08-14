import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys

fin1 = open('torchnet_test_loss.log')
fin = open('torchnet_test_baseline.log')

bl = []
for i in fin:
	bl.append(i[:-1])
ar = []
for i in fin1:
	ar.append(i[:-1])

acc = {}
ar = [float(x) for x in ar]
epnum = int(len(ar)/200)
for i in range(epnum):
	acc[i] = ar[i*200: (i+1)*200]
##baseline VS last episode

t = range(0, 200)

plt.title('')
plt.ylabel('Accuracy(%)')
plt.xlabel('Epoch')
plt.plot(t, bl, label='baseline')
for i in range(epnum):
	plt.plot(t, acc[i], label='qan'+str(i))
plt.legend(loc='lower right')

plt.savefig('epi.pdf')


