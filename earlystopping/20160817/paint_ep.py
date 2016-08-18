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
	acc = i[:-1]
	if acc == 'episode_end':
		tmp = [float(x) for x in tmp]
		if index % 2 == 1: #train
			train.append(tmp)
		else: #test
			test.append(tmp)
		index += 1
		tmp = []
		continue
	tmp.append(acc)

##baseline VS last episode

plt.title('haha')
plt.xlabel('epoch')
plt.ylabel('acc')
eptest = []
for idx in range(len(test)):
	y = test[idx][:-1]
	eptest.append(y[-1])
t = range(len(eptest))
plt.plot(t, eptest, label=str(idx))

plt.savefig('epacc.jpg')


