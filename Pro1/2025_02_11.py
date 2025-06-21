# import pygame
import logging

# __name__
# print(__name__)
# print(__file__)
# print(__doc__)
# print(__package__)
#
# if __name__ == '__main__':
#     print(__name__)

# class Student:
#     count = 0  # 类变量
#
#     def __init__(self, name, height, weight):
#         self.name = name
#         self.height = height
#         self.__weight = weight  # 实例变量
#         Student.count += 1  # 每创建一个实例，类变量count加1
#
#     def __del__(self):
#         Student.count -= 1  # 每删除一个实例，类变量count减1
#
#     # 类方法
#     # 该类的所有实例个数
#     @classmethod
#     def numbers_of_students(cls):
#         print(f"the numbers of students are: {cls.count}.")
#
#     # 实例方法
#     # 吃东西
#     def eat(self):
#         print(f"{self.name} is eating.")
#
#     # 喝水
#     def drink(self):
#         print(f"{self.name} is drunk.")
#
#     # 实例方法-get_weight
#     def get_weight(self):
#         return self.__weight
#
#     # 实例方法-set_weight
#     def set_weight(self, weight):
#         self.__weight = weight
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     # setter,须在property后面
#     @weight.setter
#     def weight(self, weight):
#         self.__weight = weight
#
# #类的内部属性
# print(Student.__dict__)
# #类的文档说明
# print(Student.__doc__)
# #类名
# print(Student.__name__)
# #类定义的模块的名称
# print(Student.__module__)
# #类的属性和方法
# print(Student.__dict__)
# #类的父类的构成元素
# print(Student.__bases__)
# #类的继承顺序
# print(Student.__mro__)


###################################################3


# class Animal:
#     count = 0  # 类变量
#
#     def __init__(self, weight, height):
#         self.weight = weight
#         self.height = height
#         Animal.count += 1  # 每创建一个实例，类变量count加1
#
#     def __del__(self):
#         Animal.count -= 1  # 每删除一个实例，类变量count减1
#
#     def get_count(self):
#         print(f"the numbers of animals are:{self.count}")
#
#
# class Dog(Animal):  # 狗类-继承自动物类
#     def __init__(self, weight, height, name):
#         super().__init__(weight, height)
#         self.name = name
#         Animal.count += 1  # 每创建一个实例，类变量count加1
#
#     def __del__(self):
#         Animal.count -= 1  # 每删除一个实例，类变量count减1
#
#     def call(self):
#         print(f"dog-{self.name} is calling")
#
#
# class Cat(Animal):  # 猫类-继承自动物类
#     def __init__(self, weight, height, name):
#         super().__init__(weight, height)  # 调用父类的构造函数
#         self.name = name
#         Animal.count += 1  # 每创建一个实例，类变量count加1
#
#     def __del__(self):
#         Animal.count -= 1  # 每删除一个实例，类变量count减1
#
#     def call(self):
#         print(f"cat-{self.name} is calling")
#
#
# # Animal.numbers_of_animals = classmethod(lambda cls: print(f"the numbers of animals are: {cls.count}."))
# animal1 = Animal(10, 20)
# animal1.get_count()
# dog1 = Dog(30, 40, "wang cai")
# cat1 = Cat(50, 60, "xiao mao")

######################################################################

# try:
#     r = 5 / 0
# except ZeroDivisionError as e:
#     logging.exception(e)
# finally:
#     print("unknown error")

# def add(a,b):
#     if not isinstance(a,int) or not isinstance(b,int):
#         raise Exception("the type of args are error")
#     return a+b
# add(1,"1")


#异常处理
# all exception are based BaseException
# try...except
# try...except...except...
# try...except...finally...
# try...except...else...finally...


# 文件读写
# fd = open("./test.py", "w", encoding="UTF-8")
# fd.writelines([
#     "'hello world'\n",
#     "'i am stark'\n",
#     "'i am from NEPU'\n"
# ])
# fd.close()
#
# fd = open("./test.py", "r", encoding="UTF-8")
# # print(fd.read())
# # print(fd.readline())
# print(fd.readlines())
# fd.close()