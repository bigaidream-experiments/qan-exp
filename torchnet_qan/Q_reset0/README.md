## Ques
1. Why do this exp?
2. What I want to verify?
3. What is the expected result?
4. Actual result
5. Next plan

---

1. Check Q value.
2. 验证Q值的变化，验证是不是需要meta-momentum DQN才能学到东西.
3. Q is increasing, and CNN test acc is increasing too.
4. Q值持续增加，CNN测试准确率有提升，但是也有抖动，大致来看是逐渐提升的，还需要观察更多的episode.
5. 修复运行到一半卡住的bug，跑更多个episode，看是否准确率会持续提高，速度会持续加快.

---

## Settings
* max_epoch=5(each episode has 5 epoch)
* max_reward=100, min_reward=-1
* one line in Q.log = average maximum action-value in one episode.
* learn_start=1000 (start to learn after 1000 steps)
* max_lr=1, min_lr=0.01, lr_delta=0.01
* add_momentum=0 (mean not use meta-momentum)
* early_stop=false
