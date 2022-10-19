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


# 创建对象
stu_1 = Students()
stu_1.name = "王"
stu_1.age = 18
stu_1.school = "武隆中学"


