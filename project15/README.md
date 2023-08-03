# implement sm2 2P sign with real network communication

## 1 代码分析

server：作为签名辅助方，负责接收client的请求，生成并保存子私钥之一的d2，完成一些辅助client签名的计算，并向其发送辅助的数据。

client：作为签名发起方，生成并保存子私钥之一的d1，请求server完成需要的辅助工作，并针对消息M完成SM2 2P sign。

## 2 运行结果

![1](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/39ec7402-3aa3-4526-bfd7-592f0f462b60)

![2](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/6fed948e-6023-4279-8ee0-8121ff86bee0)
