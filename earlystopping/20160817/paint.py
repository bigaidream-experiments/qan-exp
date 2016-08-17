import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import numpy as np

fin1 = open('torchnet_test_loss.log_100mo_10epo')
fin2 = open('validation_loss.log_100mo_10epo')

test = []
train = []
index = 1
tmp = []
for i in fin1:
	if i == 'episode':
		tmp = [float(x) for x in tmp]
		if index % 2 == 1: #train
			train.append(tmp)
		else: #test
			test.append(tmp)
		index += 1
		tmp = []
		continue
	tmp.append(i[:-1])

##baseline VS last episode

plt.title('haha')
plt.xlabel('epoch')
plt.ylabel('acc')
for idx in range(len(test)):
	t = range(0, len(test[idx]))
	y = test[idx]
	print(y)
	plt.plot(t, y, label=str(idx))
	plt.legend(loc='lower right')

plt.savefig('acc.jpg')


