# 字典推导式
# dict={key_expression : value_expression for item in iterable if condition}
# from Tools.scripts.make_ctype import values

# dict1 = {
#     "name":"ZHANGSAN",
#     "addr":"BeiJing"
# }
#
# dict2 = {
#     key:value.lower()
#     for key,value in dict1.items()
# }
# print(dict2)


# 元组推导式（生成器）
# list1 = [1, 4, 5, 6, 7]
# list2 = [item * 2 for item in list1]
# print(type(list2))  # 列表类型
# tuple2 = (item * 2 for item in list1)
# print(type(tuple2))  # 生成器类型
#
# print(next(tuple2))  # 访问生成器
# print(next(tuple2))  # 访问生成器
# print(next(tuple2))  # 访问生成器
# # print(next(tuple2))  # 访问生成器
# # print(next(tuple2))  # 访问生成器
# # print(next(tuple2))  # 访问生成器-err，访问完了
#
# for item in tuple2:
#     print(item)


###########################################################
# 函数
# def vf():
#     pass  # 空占位符
#
#
# def add(a, b):
#     '''
#
#     :param a: adder1
#     :param b: adder2
#     :return: a+b
#     '''
#     if type(a)!=type(b):return
#     else: return a + b


# def add(a, b):
#     # 如果a、b的类型不是int，err-返回
#     # type()只能求Python内置数据类型，自定义类不能推导
#     if not isinstance(a, int) or not isinstance(b, int): return
#     return a + b

# #缺省参数
# def add(a, b, c=None):
#     if c:
#         return a + b + c
#     else:
#         return a + b
#
# print(add(10,20))

# def cal(a, b):
#     return 2 * a + b
# print(cal(b=10, a=20))


# # 不定长参数组
# # 元组参数组：参数前加*
# # *args必须放在普通参数之后
# def func(argc, *args):
#     print(args)
#
#
# func(1, 2)
# func(3, 2, 3, 5)
#
#
# # 字典参数组：参数前加**
# # **kwargs必须放在*args后
# def func(**kwargs):
#     print(kwargs)
#
#
# func(a=1, b=2)
# func(a=1, b=2, c=3)
#
#
# # 传入任意参数
# def omnipotent_func(*args, **kwargs):
#     pass

# 解包
# def func(a, b, c):
#     print(f"a:{a}, b:{b}, c:{c}")
#
#
# list1 = [1, 2, 3]
# func(list1[0], list1[1], list1[2])  # 传统，麻烦
# func(*list1)  # 解包
#
# dict1 = {"a": 'a', "b": 'b', "c": 'c'}
# func(**dict1)  # 解包

# def func2(x, y, *args, **kwargs):
#     print(x, y, args, kwargs)
#
#
# func2(1, 2, {"a": 1, "b": 2})  # 字典类型传入第一个参数
# func2(1, 2, dict2={"a": 1, "b": 2})  # 指定参数名传入第二个参数


# 设计一个函数，支持传任意多个参数，函数功能为打印传入参数的乘积
# def product(*args):
#     result = 1
#     for i in args:
#         if isinstance(i, (int,float)):
#             result *= i
#         else:
#             print("参数类型错误，请输入数字类型参数")
#             return None
#     print(result)

# def multiply(*args):
#     result = 1
#     if not args:
#         print("参数不能为空")
#         return None
#
#     for i in args:
#         if not isinstance(i, (int, float)):
#             print("参数类型错误，请输入数字类型参数")
#             return None
#         result *= i
#     return result

# multiply(1.5, 2.8, 10, 0.2)  # 3.0*2.8=8.4
# multiply(1, 2, 3, 4, 5)  # 120
# multiply(1, 2, 3, "s")  # "ssssss"
# multiply(1, 2, 3.8, "s")  # 参数类型错误，请输入数字类型参数
# multiply(1, 2, "t", "s")  # 参数类型错误，请输入数字类型参数

# 姓名="张三"
# 年龄=25
#
# print(姓名, 年龄)


# 函数作为参数
# def add(a,b,func):
#     return func(a)+func(b)
#
# print(add(-10,20,abs))


# 函数作为返回值
# def func_add_creator(a,b):
#     def add():
#         return a+b
#     return add
#
# f = func_add_creator(10,20)
# print(type(f))
# print(f)
# print(f())

# # 函数标注- 只是作为提示
# def func(a: int, b: int) -> str:
#     '''
#
#     :param a: addend1
#     :param b: addend2
#     :return: a+b
#     '''
#     return a + b
#
#
# print(func(10, 20))  # 30
# print(type(func(10, 20)))  # class 'int'
# print(func.__annotations__)  # 打印函数标注
# print(func.__doc__)  # 打印函数说明


# 匿名函数lambda
# 语法：lambda args: return_value_expression
# 匿名函数可以直接赋值给变量，也可以作为参数传入函数
# 匿名函数只能有一个表达式，不能有return语句，只能有一行代码
# 匿名函数不能修改外部变量的值

# f = lambda arg1, arg2: arg1 + arg2  # 匿名函数
# print(f(10, 20))  # 30
#
# import time
#
# time.sleep(10)
# time.sleep = lambda x: None  # 禁止程序睡眠

####################################################################

# 闭包
# 闭包就是一个函数，它可以访问外部函数的变量，并且在函数返回后，外部函数的变量依然存在
# 闭包的作用：可以保存状态，延长变量的生命周期

# # k*n+b
# def outer(k, b):
#     def inner(n):
#         return k * n + b
#
#     return inner
#
#
# f1 = outer(2, 1)  # f1(n)=2*n+1
# f2 = outer(3, 5)  # f2(n)=3*n+5
# f3 = outer(4, 7)  # f3(n)=4*n+7
# print(f1(10))


# def log(func):
#     def inner(*args, **kwargs):
#         print("函数开始执行")
#         func(*args, **kwargs)
#
#     return inner
#
# def add(a, b):
#     print(a + b)
#
# def sub(a, b):
#     print(a - b)
# _add = log(add)
# _sub = log(sub)
#
# _add(20,10)
# _sub(20,10)

# def log(func):
#     def inner(*args, **kwargs):
#         print("函数开始执行")
#         func(*args, **kwargs)
#
#     return inner
#
#
# @log
# def add(a, b):
#     print(a + b)
#
#
# @log
# def sub(a, b):
#     print(a - b)
#
#
# add(20, 10)
# sub(20, 10)

import time


def Runtime(func):
    def inner(*args, **kwargs):
        start_time = time.time()

        res = func(*args, **kwargs)
        
        end_time = time.time()
        print("函数运行时间：", end_time - start_time)
        return res

    return inner


@Runtime
def test():
    time.sleep(1)
    print("test")


test()
