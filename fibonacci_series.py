 def fib(first,second,num):
    ...:     first = first
    ...:     second = second
    ...:     result = []
    ...:     for i in range(0,num):
    ...:         third = first + second
    ...: #        result.append(first)
    ...:         result.append(second)
    ...:         first = second
    ...:         second = third
    ...:     print(result)
    ...:     return
