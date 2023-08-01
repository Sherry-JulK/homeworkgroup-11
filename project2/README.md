# implement the Rho method of reduced SM3

## 1 原理
rho算法通过设置一个函数，不断进行嵌套计算，多次运算后结果会形成一个环，从而形成碰撞。

## 2 代码分析
本项目通过gmssl库中的相关函数实现对任意字符串加密，并对其进行rho攻击测量所用时间。

## 3 运行结果
进行长度8bit与长度16bit的攻击

![1](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/e96b9905-0dd1-4e8f-b720-0a1ac1e2e4c3)
![2](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/9241577a-8373-436f-bab3-1474add82914)


## 4 结果分析
随着碰撞位数的增加，运行时间成指数级增加
