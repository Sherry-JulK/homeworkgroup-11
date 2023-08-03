# impl sm2 with RFC6979

## 1 原理

SM2是非对称加密算法，基于椭圆曲线密码的公钥密码算法标准，其密钥长度256bit，SM2采用ECC 256位的一种，其安全强度比RSA 2058位高，且运算速度快于RSA。

## 2 代码分析

pSM2.py包含SM2系统参数及一些椭圆曲线上的运算和一些其他运算。利用RFC6979.py实现SM2算法。先生成一对公私钥，对消息用公钥加密，对密文用私钥解密。

## 3 运行结果

![1](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/831d534f-7e07-4319-9022-b5494efeb234)
