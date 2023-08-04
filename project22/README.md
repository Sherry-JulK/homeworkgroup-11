# research report on MPT

## 1 原理

MPT（Merkle Patricia Trie）树，即默克尔前缀树，是默克尔树和前缀树的结合。

MPT树节点类型

MPT树的节点有以下4种类型：

1.扩展节点（Extension Node）：只能有一个子节点。

2.分支节点（Branch Node）：可以有多个节点。

3.叶子节点（Leaf Node）：没有子节点。

4.空节点：空字符串。

Key只在扩展节点和叶子节点中存在，分支节点中没有Key。Value用来存储节点数值的，不同的节点类型对应的Value值也会不同，主要如下几种情况：

1.若节点类型是叶子节点，Value值存储的是一个数据项的内容。

2.若节点类型是扩展节点，Value值存储的是孩子节点的哈希值。

3.若节点类型是分支节点，Value值存储的是刚好在分支节点结束时的值，若没有节点在分支节点中结束时，Value值没有存储数据。

## 2 代码分析

MPT树中的节点包括空节点（在代码中是一个空串）、叶子节点（leaf，表示为[key,value]的一个键值对，其中key是key的一种特殊十六进制编码，value是value的RLP编码）、扩展节点（extension，也是[key，value]的一个键值对，但是这里的value是其他节点的hash值，这个hash可以被用来查询数据库中的节点。也就是说通过hash链接到其他节点）和分支节点（branch，因为MPT树中的key被编码成一种特殊的16进制的表示，再加上最后的value，所以分支节点是一个长度为17的字典）

定义leaf类、extension类、branch类表示各种节点类型。

其中leaf类定义包括类型、键值key、value值、前缀、节点的hash值以及节点下数据的hash值。

扩展节点与叶子节点类似，只是把branch节点作为extension节点组成元素，定义extension类。

分支节点包括类型与长为17的字典，分支节点前16个元素对应着key中的16个可能的十六进制字符，如果有一个[key,value]对在这个分支节点终止，最后一个元素代表一个值，即分支节点既可以搜索路径的终止也可以是路径的中间节点，在该实验的测试代码中并未加入太多节点。

定义树的类，其中包括初始化函数、创建叶子节点、创建扩展节点、获取前缀不同处索引、添加节点、向前添加扩展节点、向后添加扩展节点、更新树的value和hash值的函数。

## 3 运行结果

![1](https://github.com/Sherry-JulK/homeworkgroup-11/assets/138464371/f4104ee4-223a-4b6c-ab44-45ea0b5d4afc)
