# Meta-Momentum on CIFAR-10 for Learning Rate (2016-08-01)

### Baselines
1. SGD without adaptive learning rate optimizer. We jsut want to see QAN does learn useful policies.
2. SGD with Adam. We want to see if QAN is better than Adam. 

### Number of epochs
Train for 100 epochs. Then turn off the random selection functionality. That is to set DQN into test mode. Then use this learned
DQN with test mode to control a CNN. 

We can have another machine with 50 epochs. 

### Meta-momentum
We initiall set the meta-momentum co-efficient to 0.001. If the initial accuracy is too high, we make it even smaller. 

We only use meta-momentum in the first 50 epochs (that is half of the total epochs). As for the machine with 50 epoch, we only use meta-momentun for the first 25 epochs. We can set more experiments if possible. E.g. 200 epochs in total with 100 meta-momentum. 

Also, we must turn off the meta-momentum when testing. 

