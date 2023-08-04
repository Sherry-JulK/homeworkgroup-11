# 山东大学 网络空间安全学院 创新创业实践课程

## 肖舒予 202100460024

未组队，所有项目均个人完成。

## 运行环境

* 硬件环境

处理器：12th Gen Intel(R) Core(TM) i7-12700H @ 2.40GHz

内存：16.0 GB (15.8 GB 可用) 

* 软件环境

Win 10 操作系统 

Micorosoft Visual Studio 2022

PyCharm 2022.3.2

## 完成项目

* Project1: implement the naïve birthday attack of reduced SM3

利用gmssl库中相应函数对任意字符串加密，并对其进行生日攻击并测量攻击所需要的时间。代码中对test_len=24的位数更改可以改变攻击范围。

运行结果：

![1](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/20043c4f-fbad-4642-8dfe-41e1c819c92a)
![2](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/6a37b4de-2b25-42ee-8044-cbb8d14baed8)
![3](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/7db01647-ed2d-4bcc-9e10-c6e8c7b7867f)


* Project2: implement the Rho method of reduced SM3

利用gmssl库中的相关函数对任意字符串加密，并对其进行rho攻击测量所用时间。本实验中通过输入攻击长度可获得两个随机生成的消息以及碰撞所需时间。

运行结果：

随着碰撞位数的增加，运行时间成指数级增加。

![1](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/159a5b31-75f7-446a-b02d-ae5bf10b75b2)
![2](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/e6bd49ca-68a3-4f71-8b7b-813e23fdfbfe)


* Project3: implement length extension attack for SM3, SHA256, etc.

随机生成一个消息，加密，生成一个附加消息，用加密消息的结果推算出这一次加密结束后8个向量的值，以他们作为初始向量加密m‘，得到另一个hash值，将三个值相加得到新hash值，若相等则成功。

运行结果：

![1](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/69cb53b3-97da-4503-a253-c0a5ee241240)


* Project4: do your best to optimize SM3 implementation (software)

对string extension（string str）消息扩展函数里面的两个循环进行扩展。

运行结果：

![1](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/345541dd-0008-4696-9a77-f6a61aa10a77)
![2](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/db47cdf9-b233-4cb0-bedf-a4b78dc41fdf)


* Project5: Impl Merkle Tree following RFC6962

在最底层把数据分成小的数据块，有相应的hash和它对应。从叶子节点向上计算时，将相邻的两个hash合并成一个字符串，然后运算这个字符串的hash，这样每两个hash形成一个子hash。如果最底层的hash总数是单数，最后一定有一个hash不能和其他的合并，直接对它进行hash运算得到子hash就可以。按照上述方法循环向上进行合并，最终形成一颗倒挂的树。

运行结果：

![1](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/f36686ee-406b-4293-b099-d36d6b927421)


* Project10: report on the application of this deduce technique in Ethereum with ECDSA

根据sm2签名的特定表达式可以从签名(r,s)中推导出Pk的表达式，在标准的sm2签名中也会用到公钥信息做哈希，但是在gmssl中实现时sm2签名就是字节类型消息转化成int类型得到，所以可以从sm2签名中获得公钥，完成的sm2签名可以抵抗这种获得公钥的方法。

运行结果：

![1](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/37e7db53-acd0-42b7-a8a9-961836cc9ffe)


* Project11: impl sm2 with RFC6979

利用代码实现sm2算法，先生成一对公私钥，对消息用公钥加密，对密文用私钥解密。

运行结果：

![1](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/16ea70ae-6f3e-4486-98e0-8e96b64f5196)


* Project12: verify the above pitfalls with proof-of-concept code

①用SM2签名算法对不同消息签名但使用了相同的随机数k时，通过公式推导发现私钥d已经泄露。

②分别用SM2和ECDSA两种签名算法对同一消息签名时，如果随机数k相同也会导致私钥d泄露。

通过运行文件观察求出的私钥d是否与最初生成的一致。

运行结果：

![1](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/5817025d-782b-4bfe-8a4e-a815bfb4d973)


* Project13: Implement the above ECMH scheme

主函数中定义椭圆曲线的相关参数，前面部分定义椭圆曲线中加法函数，乘以常数函数以及求取集合哈希的函数，将调用SM3得到的哈希值作为椭圆曲线的横坐标，利用Tonelli-Shanks算法求二次剩余得到纵坐标值，充分利用了椭圆曲线上加法可逆的性质，并调用求集合哈希的函数验证，符合椭圆曲线加法运算可逆的性质。

运行结果：

![1](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/b490f74e-7c8f-4938-936e-84b6c7381c44)


* Project14: Implement a PGP scheme with SM2

import SM2，利用来自网络的SM4算法，算法中假设A向B发送消息，对其进行加解密。

运行结果：

![1](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/96b8e16b-24fe-4df3-b80a-9be840e66213)
![2](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/bf8ac3a8-755b-4bbf-b99c-7ad36025aa05)


* Project15: implement sm2 2P sign with real network communication

server：作为签名辅助方，负责接收client的请求，生成并保存子私钥之一的d2，完成一些辅助client签名的计算，并向其发送辅助的数据。

client：作为签名发起方，生成并保存子私钥之一的d1，请求server完成需要的辅助工作，并针对消息M完成SM2 2P sign。

运行结果：

![1](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/3930b342-5ae8-4414-a042-ab474f973493)
![2](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/114b64cd-a56d-4911-9aa8-028d596ee1c3)


* Project16: implement sm2 2P decrypt with real network communication

server：作为解密辅助方，负责接收client的请求，生成并保存子私钥之一的d2，计算并公布双方子私钥对应的公钥，完成一些辅助client解密的计算，并向其发送辅助的数据。

client：作为解密发起方，生成并保存子私钥之一的d1，请求server完成需要的辅助工作，并针对使用server公布的公钥加密的密文完成SM2 2P decrypt。

运行结果：

![1](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/7c7ca829-b992-4dd8-bc1f-8b230bbcc954)
![2](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/8ac84af1-dec5-4c72-87f8-e2f50db20eaf)


*Project19: forge a signature to pretend that you are Satoshi

在ECDSA签名算法中执行验证算法时，根据收到的签名(r,s)以及公开的e，P，G等信息进行验证，其中e=Hash（m），由于哈希函数的单向性我们不需要也无法通过验证签名检查消息m的信息。这样我们在已知了Bitcoin网络中某个人用自己的私钥d对一个消息签名得到一对签名(r,s)后，可以使用特定算法构造出另一个对(r',s')也为由d生成的合法签名。

运行结果：

![1](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/ed0888b0-4a8f-4eb0-8a24-04e9d863d51d)


*Project22: research report on MPT

MPT树中的节点包括空节点（在代码中是一个空串）、叶子节点（leaf，表示为[key,value]的一个键值对，其中key是key的一种特殊十六进制编码，value是value的RLP编码）、扩展节点（extension，也是[key，value]的一个键值对，但是这里的value是其他节点的hash值，这个hash可以被用来查询数据库中的节点。也就是说通过hash链接到其他节点）和分支节点（branch，因为MPT树中的key被编码成一种特殊的16进制的表示，再加上最后的value，所以分支节点是一个长度为17的字典）

定义leaf类、extension类、branch类表示各种节点类型。

其中leaf类定义包括类型、键值key、value值、前缀、节点的hash值以及节点下数据的hash值。

扩展节点与叶子节点类似，只是把branch节点作为extension节点组成元素，定义extension类。

分支节点包括类型与长为17的字典，分支节点前16个元素对应着key中的16个可能的十六进制字符，如果有一个[key,value]对在这个分支节点终止，最后一个元素代表一个值，即分支节点既可以搜索路径的终止也可以是路径的中间节点，在该实验的测试代码中并未加入太多节点。

定义树的类，其中包括初始化函数、创建叶子节点、创建扩展节点、获取前缀不同处索引、添加节点、向前添加扩展节点、向后添加扩展节点、更新树的value和hash值的函数。

运行结果：

![1](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/5032f3e1-db1c-403a-956f-23c7e8884685)


## 未完成项目

* Project6: impl this protocol with actual network communication

* Project7: Try to Implement this scheme

* Project8: AES impl with ARM instruction

* Project9: AES / SM4 software implementation

* Project17：比较Firefox和谷歌的记住密码插件的实现区别

* Project18: send a tx on Bitcoin testnet, and parse the tx data down to every bit, better write script yourself

* Project21: Schnorr Bacth

