# do your best to optimize SM3 implementation (software)

## 1 原理

循环展开最常用来降低循环开销，为具有多个功能单元的处理器提供指令级并行。也有利于指令流水线的调度。

## 2 代码分析

对string extension（string str）消息扩展函数里面的两个循环进行扩展。

## 3 运行结果

经过循环展开后时间有所提升。

![1](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/e3db1f8f-e035-48d4-9194-38b0224fbd1f)
![2](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/a78a776c-d78e-41b6-a650-e69f8c6f23bb)
