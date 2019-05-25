from django.test import TestCase

# Create your tests here.

# 冒泡排序
l = [23, 43, 12, 5, 56, 34, 65, 76, 54, 86, 54, 88, 35]
# print(len(l))
# res = []
# for i in range(len(l)-1):
#     for j in range(i+1, len(l)):
#         if l[i] > l[j]:
#             ret = l[i]
#             l[i] = l[j]
#             l[j] = ret
# print(l)

# 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('%d*%d=%d' % (j, i, j*i), end=' ')
#     print('\n')

# 斐波那契


# def fn(n):
#     if n <= 2:
#         return 1
#     else:
#         return fn(n-1)+fn(n-2)
# ret = fn(6)
# print(ret)

# res = []
#
# for i in range(1, 10):
#     res.append(fn(i))
# print(res)
# a=0
# b=1
# while b <= 10:
#     a, b = b, a+b
#     print(a)

# print(' '.join('htrehreh'))


lst = [1, 4, 5, 9, 5, 7, 13, 4, 7, 13]
# res = set(lst)
# print(res)
# new_lst = list(res)
# print(new_lst)

print([i+10 for i in lst])

print(list(set(lst)))
# n=1
# # for i in range(len(lst)-n):
# #     for j in range(len(lst)-n):
# #
# #         if lst[j] == lst[i]:
# #             res = lst.pop(j)
# #             if res:
# #                 n += 1
# # print(lst)
# lst.sort()
# print(lst)
# new = []
# for i in range(0, len(lst)-1, 1):
#     if lst[i] == lst[i+1]:
#        new.append(i)
# print(lst)
# print(new)
# for a in new:
#     # print(a)
#     print(lst[a])
#     lst.pop(a)
# # print(lst)


# a = [1,2,3,5]
# for i in a:
#     print(i)

