# Owner Feng
# Time 2022/10/12 22:55
# 不定长传参

def user_info(*args):
    print(f"args的参数类型为{type(args)},内容是{args}")


user_info(1, 3, 5, '小明', '男孩')


# 不定长 - 关键字不定长 **kwargs
def user_info(**kwargs):
    print(f"args的参数类型为{type(kwargs)},内容是{kwargs}")
user_info(name = 'Kunkun', age = 12 ,)