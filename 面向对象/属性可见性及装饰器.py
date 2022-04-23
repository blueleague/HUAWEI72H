class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self,name):
        self.__name = name or '无名氏'

    def study(self, coutse_name):
        print(f'{self.__name} 正在学习{coutse_name}')


stu = Student('思琪', '18')
stu.study('Python')
# print(stu._Student__name)
