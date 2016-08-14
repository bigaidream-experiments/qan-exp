import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys

fin1 = open('torchnet_test_loss.log')


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
for i in range(epnum):
	plt.plot(t, acc[i], label='qan'+str(i))
plt.legend(loc='lower right')

plt.savefig('epi.pdf')


