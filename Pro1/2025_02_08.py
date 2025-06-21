# 数据类型- 序列：列表

# # 数据类型可以混合存入
# list1 =[1,"hello",1.23,True,["World",1]]
# print(list1)  # 输出整个list1
# # 访问：-n ~ n-1
# # 负数索引代表从后往前查第n个
# print(list1[-2])  # 输出True
# #嵌套访问：
# print(list1[-1][0])  # 输出["World",1]中的1

# list1 = [1, 5, 8, 7]
# #添加append
# list1.append(4)
# print(list1)
# list1.insert(2,10)
# print(list1)

# list1 = [1, 5, 8, 7]
# list2 = [1,2,3,4]
# list1.append(list2)  # 将list2作为整体插入list1末尾
# print(list1)
#
# #扩展extend
# list1 = [1, 5, 8, 7]
# list2 = [1,2,3,4]
# list1.extend(list2)  # 将list2中的元素插入list1末尾中
# print(list1)


# list.append(): 将整个对象作为一个整体添加到列表中
# list.extend(): 将可迭代对象的每个元素逐个添加到列表中
####################################################


# 删除
# #remove 删除列表中第一个与指定元素相同的元素
# list1 = [1, 5, 8, 7,8]
# # list1.remove(8)
# # print(list1)
# for item in list1:
#     if item>6:
#         list1.remove(item) #并没有将7删除，而是只删除了第一个8
# print(list1)

# # pop 删除列表中指定下标位置的元素并返回被删除的元素，默认为最后一个元素
# list1=[1,5,7,5]
# a = list1.pop(2)
# print(list1)
# print(a)

# # del
# list1=[1,5,7,5]
# del list1[1]
# print(list1)

# # clear 清空
# list1 = [1,2,3,4,5]
# list1.clear()
# print(list1)


#####################################
# # 列表截取，切片操作
# # 基本语法：[start:stop:step],从索引为start开始到stop-1，每隔step取一次(默认为1)
# list1 = [1,5,8,7]
# print(list1[1:3]) #[5, 8]
# print(list1[1:]) #[5, 8, 7]
# print(list1[:2]) #[1, 5]
# print(list1[1:4:2])  #[5, 7]
#
# a="hello"
# print(a[1:4:2])  #"el"

# list1=[1,5,8,7]
# for item in list1:
#     print(item)  # 只有值
# for i,item in enumerate(list1):
#     print(i,item)  # 带索引

#####################################
# #排序
# list1=[1,5,8,7]
# list1.reverse() # 逆序
# print(list1)
#
# list1.sort()    # 正序
# print(list1)
#
# list1.sort(reverse=True)    # 倒序
# print(list1)

# # 直接赋值:对象的引用
# list1=[1,5,8,7]
# list2 = list1
# print(list2)
# list1[2]=10
# print(list2)
#
# # 浅拷贝:拷贝对象
# list1 = [1,5,8,7]
# list2 = list1.copy()
# print(list2)
# list1[0] = 10
# print(list1)
# print(list2)


# # 浅拷贝:拷贝对象,不拷贝对象内部的子对象
# list1 = [1,5,8,7,[0,3]]
# list2 = list1.copy()
#
# list1[4][0]=10
# print(list2)


# # 深拷贝:完全拷贝对象及其子对象
# import copy
# list1 = [1,5,8,7,[0,3]]
# list2 = copy.deepcopy(list1)
# list1[4][0]=10
# print(list2)

##########################################3
# #字符串转列表
# a="hello"
# print(list(a)) #强制转换
#
#
# #列表转字符串
# list1 = ['h','e','l','l','o']
# print("".join(list1))

##############################################

# # 660判断是否回文
# list1 = list(input())
# list2 = list1.copy()
# list1.reverse()
# print(1) if list1 == list2 else print(0)

# # 674换行输出字符串单词
# list_word = list(input().split(" "))
# for item in list_word:
#   print(item)

##########################################################


#########################################################
# # 序列函数
# num_list1 = [1, 5, 8, 7]
# str_hello = "hello"
#
# # len()
# print(len(str_hello))
#
# # 判断元素是否在序列中：  ...in...
# # 判断元素是否不在序列：  ...not in...
# print(1 in num_list1)
# print(9 not in num_list1)
#
# # max() min()
# print(max(num_list1))
# print(min(num_list1))
#
# # count()
# print(num_list1.count(1), str_hello.count('l'))
#
# # index()
# print(str_hello.index('l', 0, 4))  # 从0-4找第一个'l'的位置

##################################################################

# 字典 dict-特点：无序
# dict1 = {
#     # key 是不可变类型
#     "name": "张三",
#     "age": 20,
#     "dict1": {'a': 1},
#
#     "friends": [
#         {"id": 123, "name": "a"},
#         {"id": 456, "name": "b"}
#     ]
# }
# # #获取字典中的元素
# # #通过key-如果没有对应值，报错
# # print(dict1["name"])
# # #get方法-如果没有对应值，不报错，返回None，可以设置返回默认值
# # print(dict1.get("name1","return_default"))
#
# # 遍历
# # 遍历键
# for k in dict1.keys():  # 直接使用dict1,默认也是遍历键
#     print(k)
# # 遍历键值
# for item in dict1.items():
#     print(item)
# # 遍历值
# for v in dict1.values():
#     print(v)

# 删除- pop() - del -
# 修改- 键访问 - update():有则改、无则加

