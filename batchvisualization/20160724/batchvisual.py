import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys

fin = open('batchselection.log') 

a = {}
for i in range(1,11):
	a[i] = []

for l in fin:
	tokens = l.split()
	nums = [int(x) for x in tokens]
	print(nums)
	for i in range(1,11):
		a[i].append(0)
	for i in nums:
		a[i][len(a[i])-1] += 1

t = range(len(a[1]))

plt.title('batch visualization')
plt.ylabel('number')
plt.xlabel('Iteration')
label = {}
for i in range(1,11):
	label[i] = str(i)
for i in range(1,11):
	#print (a[i])	
	plt.plot(t, a[i], label=label[i])

plt.legend(loc = 'lower right')

plt.savefig('batchvisual.pdf')
