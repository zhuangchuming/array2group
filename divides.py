# !/usr/bin/python  
# -*- coding:utf-8 -*-
# encoding: utf-8

import random

length = input('请输入要产生的随机数个数：')


# print(random.randint(12, 20))
def rand():
    arr = []#保存所有才生的原始数据
    t = int(length)
    for x in range(t):
    	arr.append(random.randint(1, 500))
    new_ls = sorted(arr,reverse=True) #从大到小排序后数组
    # new_ls = [469, 315, 209]
    # new_ls = [473, 348]
    # new_ls = [394, 149, 53]
    # new_ls = [302, 298, 129]
    print(new_ls)
    global minimsize
    # 总和
    total = sum(new_ls)
    print('总和:', total)

    # 中间值
    half = int(total / 2)
    print('和的中间值:', half)

    # 两个组
    group1 = []
    group2 = []

    minim = half  # 与中间值的差的最小值
    addPosition = 0  # 记录前面相加的值与中间值的差最小值的对应new_ls位置

    st = 0

    # 对排序过的进行一个
    for index, value in enumerate(new_ls):
        st = st + value
        m = half - st
        if m > 0 and m < minim:
            minim = m
            group1.append(value)  # 前面的数的列表
        else:
            group2 = new_ls[index:len(new_ls)]  # 后面的数的列表
            addPosition = index - 1;
            break;
    # 保证g2的综合要大于
    g1 = sum(group1)
    g2 = sum(group2)
    print(group1, '总和：', g1, "   长度：", len(group1))
    print(group2, '总和：', g2, "   长度：", len(group2))

    # 差值
    t1 = abs(g1 - g2)
    # 差值的中间值，因为需要知道这个值在排序数组中的位置索引
    t1h = int(t1 / 2)
    print("group1-group2 = ", t1, "    差值的中间值: ", t1h)
    minimsize = t1
    t1position = len(new_ls)  # 定位差值的位置
    for index, value in enumerate(new_ls):
        if t1 > value:
            t1position = index
            print("差值所在列表的排序位置：", t1position)
            break
    t1hposition = len(new_ls)  # 定位差值的一半的位置
    for index, value in enumerate(new_ls):
        if t1h > value:
            t1hposition = index
            print("差值一半所在列表的排序位置：", t1hposition)
            break
    print('t1hposition', t1hposition, t1position)
    outputMini(new_ls, group1, group2, t1, t1h, t1position, t1hposition)


halfval = 0;  # 中间值的一半
minimsize = 0;  # 输出最小的值
miniposition = []


def outputMini(new_ls, group1, group2, t1, t1h, t1position, t1hposition):
    # print('\n')
    global miniposition
    global minimsize
    global halfval
    # 求最小单项
    # 把离中间值最接近的上下位数记做最小值
    if  t1hposition != len(new_ls):
        if  t1hposition < len(new_ls) and abs(t1h - new_ls[t1hposition]) < minimsize:# 记录单项左边的位置
            minimsize = abs(t1h - new_ls[t1hposition])
            miniposition = [len(new_ls) - t1hposition]

        if  t1hposition - 1 < len(new_ls) and abs(t1h - new_ls[t1hposition-1]) < minimsize:# 记录单项右边的位置
            minimsize = abs(t1h - new_ls[t1hposition-1])
            miniposition = [len(new_ls) - t1hposition+1]

    print("最小值单项差值：", minimsize, "以及倒数位置：", miniposition)

    # 最小多项差值,组合的数一定在差值一半之后的位置中
    t1hList = new_ls[t1hposition:len(new_ls)]
    print("差值的中间值后面的列表：", t1hList, "长度：", len(t1hList))

    halfval = t1h
    if len(t1hList) >= 2:
        for ind in range(len(t1hList)):  # 这一级表示指针数
            if ind >= 1:
                roundfor(t1hList, ind + 1, 0)
                if minimsize == 0:
                    break;
    print('最小值是：', minimsize, "     数组倒数位置是：", miniposition)

    g2 = group2.copy()  # 拷贝数据
    # 处理数据，形成新的数组
    for ind, value in enumerate(miniposition):
        group1.append(group2[len(group2) - value])  # 先更新group1
        del g2[len(group2) - value]
    group2 = g2
    g1 = sum(group1)
    g2 = sum(group2)
    print(group1, '新的总和：', g1, "   长度：", len(group1))
    print(group2, '新的总和：', g2, "   长度：", len(group2))
    print('\n')
    print("他们的差值：", abs(g1 - g2))
    print('\n\n\n\n\n\n')


#	list 为要循环的列表
#	index 为指针数，也可以理解为要递归的次数
#	val 上一级的值，如果是多级，表示多级之前的值的和
#	return 返回形成组合的值位置，这个位置是相对于数组最后一位往前数
def roundfor(list, index, val):
    position = 0  # 当前循环中最小值的位置
    hasmini = False
    global miniposition
    global minimsize
    global halfval
    for ind, value in enumerate(list):
        if index > 1:  # 继续递归循环
            if ind + index <= len(list):
                # if len(list) > 1 and ind +1 <= len(list)-1:
                po = roundfor(list[ind + 1:len(list)], index - 1, val + value)
                if po:  # 判断是否有新的较小值
                    hasmini = po
                    miniposition.append(len(list) - ind)
                if minimsize == 0:  # 如果找到0则提前结束循环
                    return True
        else:  # 最深一层的起点
            if abs(halfval - val - value) < minimsize:
                minimsize = abs(halfval - val - value)
                position = len(list) - ind
                miniposition = [position]  # 有更小值时，更新一个数组
                hasmini = True
                print('较小值是：', minimsize, "倒数的位置：", position)
                if minimsize == 0:  # 值为0时就认为是最小的
                    return True
    return hasmini


if __name__ == '__main__':
    rand()
