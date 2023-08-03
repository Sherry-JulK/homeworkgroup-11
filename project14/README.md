# Implement a PGP scheme with SM2

## 1 原理

消息方发送随机生成对称加密的会话密钥sessionkey，并用接收方的SM2公钥加密sessionkey，用sessionkey加密消息，同时发送给接收方。接收方收到两个密文，先用自己的SM2私钥解出会话密钥sessionkey，再利用sessionkey解对称密码得到消息明文。

## 2 代码分析

首先要import SM2，然后利用来自网络的SM4算法。算法中假设A向B发送消息，对其进行加解密。

![2](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/815743a1-4690-4a01-910e-17af2cfed2ad)


## 3 运行结果

![1](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/e4bf4f93-269a-48ed-86a6-7a90f4d91771)
