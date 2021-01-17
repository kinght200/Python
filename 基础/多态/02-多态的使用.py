class Dog(object):
    def work(self):
        print('狗正在工作')


class PoliceDog(Dog):
    def work(self):
        print('警犬正在攻击敌人')


class BlindDog(Dog):
    def work(self):
        print('导盲犬正在领路')


class DrugDog(Dog):
    def work(self):
        print('缉毒犬正在搜毒')


class Person(object):
    def __init__(self, name):
        self.name = name

    def work_with_dog(self):
        self.dog.work()


p = Person('张三')

pd = PoliceDog()
p.dog = pd
p.work_with_dog()

bd = BlindDog()
p.dog = bd
p.work_with_dog()

dd = DrugDog()
p.dog = dd
p.work_with_dog()
