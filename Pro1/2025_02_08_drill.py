# my_dict = dict()
# alist = list(input().split())
# for item in alist:
#     my_dict.update({item: alist.count(item)})
#
# print(my_dict)  # my_dict是键值对构成的集合
# for item in my_dict.items():  # item是一个键值对
#     print(item)

# # 设计一个电话簿查询，输入人名输出电话号
# phone_dict = {
#     "zhangsan": "13300110011",
#     "lisi": "15511223344",
#     "luo": "17745456767",
#     "lihua": "18877668899",
#     "jack": "16645674567"
# }
# while True:
#     connect_name = input("Please input user's name:")
#     if connect_name == "exit": break
#     print(phone_dict.get(connect_name, "users does not exist"))

# 数据类型 -序列：集合
# #一组key的集合，key不重复,且自动排序
# set1={"name","age","weight"}
# print(set1)
# set1.add(123)
# print(set1)


# list1 = [1, 5, 8, 7]
# list2 = []
# for item in list1:
#     list2.append(item * 2)
# print(list2)

# 列表推导式
# [expression for item in list if condition]

# list1 = [1, 5, 8, 7]
# # list2 = [item * 2 for item in list1 if item%2==1]
# list2 = [item*2 if item%2==1 else item/2 for item in list1]
# print(list2)
#
# list2 = [(i,j) for i in range(1,4) for j in range(5,8)]
# print(list2)


# str1, str2 = input().split(" ")
# res_list = [s1 + s2 for s1 in str1 for s2 in str2]
# res_list = [f"{s1}{s2}" for s1 in str1 for s2 in str2]
# res_list = ["".join([s1,s2]) for s1 in str1 for s2 in str2]
# res_list = ["%s%s"%(s1,s2) for s1 in str1 for s2 in str2]
# print(res_list)

# str1, str2 = input().split()
# print([f"{s1}{s2}" for s1 in str1 for s2 in str2])

# stu_dict = {  # 学生成绩字典
#     "jack": 90,
#     "pony": 50,
#     "li": 70,
#     "wang": 60
# }
# # 遍历键填充结果
# print([f"{key}={stu_dict[key]}" for key in stu_dict.keys() if stu_dict[key] < 80])
# # 遍历键值填充结果
# print([f"{key}={val}" for key, val in stu_dict.items() if val < 80])

