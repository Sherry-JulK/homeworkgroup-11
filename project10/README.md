# report on the application of this deduce technique in Ethereum with ECDSA

## 1 原理

椭圆曲线数字签名算法（ECDSA）是使用椭圆曲线密码（ECC）对数字签名算法（DSA）的模拟。与普通的离散对数问题（discrete logarithm problem DLP）和大数分解问题（integer factorization problem IFP）不同，椭圆曲线离散对数问题（elliptic curve discrete logarithm problem ECDLP）没有亚指数时间的解决方法。因此椭圆曲线密码的单位比特强度要高于其他公钥体制。
ECDSA是ECC与DSA的结合，整个签名过程与DSA类似，所不一样的是签名中采取的算法为ECC，最后签名出来的值也是分为r,s。

签名过程如下：

1、选择一条椭圆曲线Ep(a,b)，和基点G；

2、选择私有密钥k（k<n，n为G的阶），利用基点G计算公开密钥K=kG；

3、产生一个随机整数r（r<n），计算点R=rG；

4、将原数据和点R的坐标值x,y作为参数，计算SHA1做为hash，即Hash=SHA1(原数据,x,y)；

5、计算s≡r - Hash * k (mod n)

6、r和s做为签名值，如果r和s其中一个为0，重新从第3步开始执行

验证过程如下：

1、接受方在收到消息(m)和签名值(r,s)后，进行以下运算

2、计算：sG+H(m)P=(x1,y1), r1≡ x1 mod p。

3、验证等式：r1 ≡ r mod p。

4、如果等式成立，接受签名，否则签名无效。

## 2 代码分析

根据sm2签名的特定表达式可以从签名（r，s）中推导出Pk的表达式。在标准的sm2签名中也会用到公钥信息做哈希，但是在gmssl中实现时sm2签名就是字节类型消息转化成int类型得到，所以可以从sm2签名中获得公钥，完整的sm2签名可以抵抗这种获得公钥的办法。

## 3 运行结果

![1](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/f45f0441-a390-49c8-8ec1-71daafa3b01e)
