#逻辑语句 使用缩进表示块作用域

#判断语句
# a = 10
# if a>0:
#     print("+",a,sep="")  #sep="" 取消两个输出之间的间隔
# elif a<0:
#     print("-",a,sep="")
# else:
#     print(a)

#按条件赋值可以写在一行
# a= a+1 if a>0 else a-1
# a=int(input())
# a = a+1 if a>0 else a-1 if a<0 else 0
# print(a)

#练习：判断闰年问题
# year=int(input())
# if year%4==0 and year%100!=0 or year%400==0:
#     print(1)
# else:
#     print(0)

#循环语句：
#for ... in ...
#for i in (0,1,2,3,4,5):
    # print(i)

#for i in (4,3,5,7,2):
    # print(i)

#for i in range(0,10)  # [0,10)左闭右开
    # print(i)

#while
# i=0
# while i<10:
#     i+=1

#计算前n项和
# mysum=0
# for i in range(0,1+int(input())):
#     mysum+=i
# print(mysum)

#求和
# print(sum(range(1,1+int(input()))))

#循环打印
# for i in range(1,100):
#     print(i,end="") if i%2==1 else print()
# for i in range(1,100,2):
#     print(i)

#判断质数
# num=int(input())
# for i in range(2,num):
#     if num%i==0:
#         print(0)
#         break
# else:
#     print(1)
#for...else 如果不是从for的遍历完的正常出口退出，如break属于异常退出时就会进入for配对的else


#打印三角形
# for i in range(1,1+int(input())):
#     for j in range(1,1+i):
#         print("*",end="")
#     print()

# for i in range(1,1+int(input())):
#     print("*" * i)

# n = int(input())
# for i in range(1,n+1):
#     print((" " * (n-i)) + ("*" * i))

# ans=0
# for i in range(1,1+int(input())):
#     ans += sum(range(1,i+1))
# print(ans)

# 在Python中，整数的二进制表示是动态的
# 负数的二进制位数取决于其存储所需要的最小位数
# n = int(input())
# count = 0
# if n<0:
#   n = n & 0xffffffff
#
# while n:
#   n = n & (n-1)
#   count += 1
# print(count)

# 在文件头部加上这行注释，防止出现中文乱码。Python2默认以ASCII编码
# -*- coding: utf-8 -*-
#######################################################
# 数据类型
# 数字
# 整型int  浮点float  布尔bool

# 序列
# 字符串:
# 拼接
# print("123"+"456")
# print("123"*5)
# print("123","456",sep="")
# #变量与字符串拼接
# a = "hello"
# b = "world"
# print("%s %s" % (a,b))
# print("{} World".format(a))
# print(f"{a} {b}")  #Python3：fstring格式
# print(a + " " + b)
#
# #取消转义字符：rstring格式
# print(r"D:\new.txt")
#
# #常用方法
# a = "hello {}"
# print(a.format("world"))
# print(a.split('l'))  #分割字符串
# print("-".join(a))  #每个字符以-分割
#
# # find查找子串
# # 子字符串，开始位置，结束位置
# print(a.find("l"))
# print(a.find("lo"))
# print(a.find("l",2,5))
#
# #判断字符串是否都是数字
# print("1231".isdigit())
# #判断字符串是否都是字母
# print("abc".isalpha())
# #是否都是大写字母
# print("ABC".isupper())
#
# #替换 replace()
# print(a.replace('l','n'))  # 全部替换
# print(a.replace('l','n',1))  # 替换1个




















