# Owner Feng
# Time 2022/10/14 10:45
# 基本捕获语法
try:
    f = open("data/test.txt", 'r', encoding="utf-8")
except:
    print("Exception")
    f = open("data/test.txt", "w", encoding="utf-8")

# 捕获指定的异常
try:
    print(name)
except NameError as e:
    print("变量未定义")

# 捕获多个异常
try:
    1/0
except(NameError, ZeroDivisionError) as e:
    print("Error!")

# 捕获全部异常
try:
    pass
except Exception as e:
    print("异常")
else:
    print("No Exception! Great!")
finally:
    print("有没有异常都会执行！")

# 异常具有传递性
#



