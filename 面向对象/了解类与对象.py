class Student:
    def study(self, course_name):
        print(f'{self}学生正在学习{course_name}')

    def play(self, play_name, v):
        print(f"{self}学生正在玩{play_name, v}游戏")
s1 = Student    #类

print(type(s1))

s1.study('wsc','韦仕昌')

s = Student()   #实例
print(type(s))
print(hex(id(s)))
s.play("王者荣耀", "v10.2.10")


