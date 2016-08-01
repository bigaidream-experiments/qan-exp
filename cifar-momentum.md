# Meta-Momentum on CIFAR-10 for Learning Rate (2016-08-01)

### Baselines
1. SGD without adaptive learning rate optimizer. We jsut want to see QAN does learn useful policies.
2. SGD with Adam. We want to see if QAN is better than Adam. 

### Number epochs
Train for 50 epochs. Then turn off the random selection functionality. That is to set DQN into test mode. Then use this learned
DQN with test mode to control a CNN. 

### Meta-momentum
We initiall set the meta-momentum co-efficient to 0.001. If the initial accuracy is too high, we make it even smaller. 

We only use meta-momentum in the first 30 epochs. 

Also, we must turn off the meta-momentum when testing. 

