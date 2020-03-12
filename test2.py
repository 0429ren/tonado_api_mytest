# -*- coding: utf-8 -*-
# -*- author: 任士梅-*-

#生成器  一边生成 一边迭代 一次只生成一个值 大大节约内存空间 通过next()函数获取返回值
# generator_ex = (x*x for x in range(10))
# print(generator_ex)


#由于不断调用next()是个很不好的习惯 一般不建议这样用
# print(next(generator_ex))
# print(next(generator_ex))
# print(next(generator_ex))
# print(next(generator_ex))
# print(next(generator_ex))
# print(next(generator_ex))
# print(next(generator_ex))
# print(next(generator_ex))
# print(next(generator_ex))
# print(next(generator_ex))

#而是用for循环遍历的方法 获取每一个返回值
# for i in generator_ex:
#     print(i)



# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         if self.a < 20:
#             x = self.a
#             self.a +=1
#             return x
#         else:
#             raise StopIteration
#
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# for i in myiter:
#     print(i)

def fib(number):
    n,a,b = 0,0,1
    while n < number:
        yield b
        a,b = b, a+b
        n = n+1
    return 'ok!'
print(fib(5))

for i in fib(5):
    print(i)





