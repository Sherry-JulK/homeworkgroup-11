# implement length extension attack for SM3, SHA256, etc.

## 1 原理

长度扩展攻击（length extension attack），是指针对某些允许包含额外信息的加密散列函数的攻击手段。对于满足以下条件的散列函数，都可以作为攻击对象：

① 加密前将待加密的明文按一定规则填充到固定长度（例如512或1024比特）的倍数；

② 按照该固定长度，将明文分块加密，并用前一个块的加密结果，作为下一块加密的初始向量（Initial Vector）。

满足上述要求的散列函数称为Merkle–Damgård散列函数（Merkle–Damgård hash function）

## 2 代码分析

随机生成一个消息，加密，生成一个附加消息，用加密消息的结果推算出这一次加密结束后8个向量的值，以他们作为初始向量加密m'，得到另一个hash值，将三个值相加得到新hash值，若相等则成功。

## 3 运行结果
![1](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/5595a390-6109-4132-a73d-0844a0d3719a)
