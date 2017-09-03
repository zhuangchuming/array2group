# array2group
注：由于部分代码运行使用到了python3，故需要你的环境中使用 如下命令来运行文件：python3 divides.py


这是一道考题：据说是各大科技公司（google,amazon,facebook）的面试以及用来培训高级程序员的题目

### 原题目如下：

![Image](https://github.com/zhuangchuming/array2group/blob/master/imgs/head.jpeg)



### 原题意思：
给你一个长度不超过100列表的正整数，且每个正整数的值都不会大于500.请编写程序，将这些正整数分成两个数组，使得这两个数组所有元素的总和的差值为最小，以下是一些例子：
eg1:
input: 1 1 1 2 2
output: (1 1 1)(2 2) => 1
(difference between 3 and 4)

eg2:
input: 1 2 4 6
output: (1 6)(2 4) => 1
(difference between 7 and 6)

divides.py 经过测试，目前暂未出现运行失败或者错误的情况，如果有想测试的，可以亲自在代码里修改：
### 步骤如下：

![Image](https://github.com/zhuangchuming/array2group/blob/master/imgs/content0.jpeg)

注释第七行，并且在17行组输入你想要测试的数组，然后运行即可。


### 解题思路：
1、排序 从大到小；
2、长度=n的排序后列表的前m位的和小于(n-m)位的和；设前m位的和=group1，后面n-m为的和为group2;
（原因：大值拿出来作和，会使得数组的和的值范围变得太大，没有意义）
3、求group1-group2 差值的中间值。  差值设为:th1
4、group2只要再取出某y位的值的和接近于th1,然后给group1就可以得出最小的两个数组。


### 运行示例如下图：

![Image](https://github.com/zhuangchuming/array2group/blob/master/imgs/content1.jpeg)


![Image](https://github.com/zhuangchuming/array2group/blob/master/imgs/content2.jpeg)
