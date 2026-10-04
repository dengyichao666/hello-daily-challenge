class Animal:
    def __init__ (self,name):
        self.name = name

    def speak(self):
        print("...")
    def info(self):
        print("我是动物")

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    def speak(self):
        print(f"{self.name}:旺旺！")
    def info(self):
        print("我是狗")
        super().info()
    def __str__(self):
        return self.name

class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
    def speak(self):
        print(f"{self.name}：喵喵！")

d = Dog("旺财")
c = Cat("喵咪")
d.speak()

print(d)
d.info()