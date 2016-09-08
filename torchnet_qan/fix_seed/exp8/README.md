## Result

![alt image](https://github.com/bigaidream-experiments/qan-exp/blob/master/torchnet_qan/fix_seed/exp8/acc.png?raw=true)


## QAs

### Questions
1. Why do this exp?
2. What do I want to verify?
3. What is the expected result?
4. Actual result
5. Next plan

---

### Answers
1. Check if finetuning works when fixing initial seed.
2. I want to verify the DQN finetune effect under the circumstance of fixing seed.
3. Average acc is increasing along with episodes.
4. Average acc increase actually, but the curve is like impulse function.
5. Modify reward function.

---

## Settings
* data=mnist
* batch_size=128
* max_epoch=5(each episode has 5 epoch)
* elapsed_episode=130
* max_reward=100, min_reward=-1
* one line in Q.log = average maximum action-value in one episode.
* learn_start=3900 (start to learn after 1000 steps)
* max_lr=0.05, min_lr=0.00001, lr_delta=10% or 50%
* add_momentum=0 (means meta-momentum is not used)
* early_stop=false (means early-stop is not used)
