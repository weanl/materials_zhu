# materials_zhu

_for DeepCache paper_

### 1. papers
[DeepCache(2018NetAI)](https://dl.acm.org/citation.cfm?id=3229555)

### 2. tutorials_of_codes/
    - seq2seq_master/

[seq2seq-tensorflow-google](https://github.com/google/seq2seq)

    - tensorflow_seq2seq_tutorials_master/  

[seq2seq-tensorflow-ematvey](https://github.com/ematvey/tensorflow-seq2seq-tutorials)

### 3. codes/
    - .py
    - readme.md

### 4. dataset1

**dataset1_v1**:  生成了一个二维数组，6*20000大小的。因为论文中zipf分布给了6个不同参数。所以访问序列就是每一个给定的参数产生20000次访问，然后参数变化，再访问20000次这样

**dataset1_v2**:  (80, 1000)  [采用蒙特卡罗方法生成zipf分布随机数据](https://www.jianshu.com/p/c35a0916a872) 

    
 **dataset1_v3**:  (80, 1000)  [生成Zipf分发的随机数](http://landcareweb.com/questions/25789/sheng-cheng-zipffen-fa-de-sui-ji-shu)-   我修改了程序重新产生了训练集，每个interval的request次数为1000，β是6个值中随机的一个，object的流行度也是随机的。一共有80个interval，共80K次访问。 


---
_END OF FILE_
