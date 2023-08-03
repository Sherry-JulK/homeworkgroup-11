# verify the above pitfalls with proof-of-concept code

## 1 代码分析

① 用SM2签名算法对不同消息签名但使用了相同的随机数k时，通过公式推导发现私钥d已经泄露。
② 分别用SM2和ECDSA两种签名算法对同一消息签名时，如果随机数k相同也会导致私钥d泄露。
通过运行文件，观察求出的私钥d是否与最初生成的一致。

## 2 运行结果

![1](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/4953f604-09fa-42da-836c-973176e0b668)
