implement the naïve birthday attack of reduced SM3

1 原理
SM3适用于商用密码应用中的数字签名和验证，是在SHA-256基础上改进实现的一种算法，其安全性和SHA-256相当。SM3和MD5的迭代过程类似，也采用Merkle-Damgard结构。消息分组长度为512位，摘要值长度为256位。整个算法的执行过程可以概括成四个步骤：消息填充、消息扩展、迭代压缩、输出结果。
生日攻击一般应用在数字签名中，一般来说为了对机密消息进行签名，因为加密的限制，如果消息很大的情况下不可能对所有消息进行签名，通常对消息计算hash值，然后对这个hash值进行签名。
SM3的输出范围是256位，那么我们攻击就是找到两个不同的x，y，让f（x）=f（y），即x和y发生了碰撞。

2 代码分析
利用gmssl库中相关函数对任意字符串加密，并对其进行生日攻击并测量攻击所需要的时间。
代码中对函数攻击前24位，可根据攻击范围对test_len = 24进行更改

3 运行结果
对sm3进行前8位，前16位，前24位进行攻击，对前8位进行攻击时由于时间太短结果为0
![image](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/2eaa249c-64b8-4228-b8d9-73a094eeecf3)
![2](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/40f38fba-6264-43a3-9e98-327dcaf225f6)
![3](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/e2c70afd-fdd0-4b87-ae70-c1cfb5d7a0d0)
