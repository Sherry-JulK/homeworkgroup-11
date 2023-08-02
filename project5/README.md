# Impl Merkle Tree following RFC6962

## 1 原理

Merkle Tree是存储hash值的一棵树。Merkle树的叶子是数据块的hash值，非叶节点是其对应子节点串联字符串的hash。

## 2 代码分析

在最底层把数据分成小的数据块，有相应的hash和它对应。从叶子节点向上计算时，将相邻的两个hash合并成一个字符串，然后运算这个字符串的hash，这样每两个hash形成一个子hash。如果最底层的hash总数是单数，最后一定有一个hash不能和其他的合并，直接对它进行hash运算得到子hash就可。按照上述方法循环向上进行合并，最终形成一颗倒挂的树。

## 3 运行结果

![1](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/9ec65dbc-fd69-452b-a40a-49bf41ada571)
