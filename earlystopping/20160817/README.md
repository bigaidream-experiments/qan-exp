#exp parameter setting

* momentum_coefficient = 0.01 (do momentum for 100 iteration, equivalent to 1/3 epoch)
* min_epoch_num = 10 (avoid using early-stopping too early)
* monitor 16 neuron (state = 16\*256\*3\*3)
* max_learningrate = 1, min_learningrate = 0.01, learningrate_delta = 0.01 (means add or subtract 0.01 by each action)
* DQN alternates between train and test, the results are all test result.
