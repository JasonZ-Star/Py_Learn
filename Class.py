# Owner Feng
# Time 2022/10/19 22:53
# 用class关键字定义
class Students:
    name = None
    age = None
    nationality = None
    school = None

    # 定义成员方法
    def say_hi(self):
        print(f"Hi，大家好，我是{self.name}")

    # str 魔术方法
    def __str__(self):
        print(f'我是{self.name},我的年龄是{self.age}')

    # lt魔术方法
    def __lt__(self, other):
        return self.age < other.age  # 不能写小于等于

    def __le__(self, other):
        return self.age <= other.age  # 可以写小于等于

    # eq魔术方法，比较两个对象是否相等
    def __eq__(self, other):
        return self.age == other.age


# 创建对象
stu_1 = Students()
stu_1.name = "王"
stu_1.age = 18
stu_1.school = "武隆中学"

stu_2 = Students()
stu_2.name = "朱"
stu_2.age = 20
stu_2.school = "白塔中学"
