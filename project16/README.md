#  implement sm2 2P decrypt with real network communication

## 1 代码分析

server:作为解密辅助方，负责接收client的请求，生成并保存子私钥之一的d2，计算并公布双方子私钥对应的公钥，完成一些辅助client解密的计算，并向其发送辅助的数据。

client：作为解密发起方，生成并保存子私钥之一的d1，请求server完成需要的辅助工作，并针对使用server公布的公钥加密的密文完成SM2 2P decrypt。

## 2 运行结果

![1](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/b006b319-db3f-49a0-a1df-5f1e86c64f28)

![2](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/ed5e9c33-32fb-4b0c-b8d1-ebf0d1c676e4)
