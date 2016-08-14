import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys

fin = open('torchnet_test_baseline.log')
fin1 = open('torchnet_test_loss.log')

ar = []
for i in fin:
    ar.append(i[:-1])

ar1 = []
for i in fin1:
	ar1.append(i[:-1])

ar = [float(x) for x in ar]
ar1 = [float(x) for x in ar1]
ar1 = ar1[0:200]
##baseline VS last episode

t = range(0, len(ar))

plt.title('')
plt.ylabel('Accuracy(%)')
plt.xlabel('Epoch')
plt.plot(t, ar, label='baseline')
plt.plot(t, ar1, label='qan')
plt.legend(loc='lower right')

plt.savefig('acc.pdf')


