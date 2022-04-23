class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}')

    def play(self):
        print(f'{self.name}正在玩游戏。')

    def __repr__(self):
        return f'姓名：{self.name}，年龄：{self.age}'  ##默认返回值，而不是反馈内存地址


stu1 = Student('韦仕昌', '38')
stu1.study('数学')
stu1.play()
print(stu1)

stu2 = Student('夏洛', '31')
print(stu2)
