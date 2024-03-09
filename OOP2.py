class Dog:
    default_name = "jack"
    default_age = 3
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} сидит")
    def roll_over(self):
        print(f"{self.name} перекатывается")  

my_dog = Dog("willie",6)
print(my_dog.name)
print(my_dog.age)
my_dog.sit()
my_dog.roll_over()
lucy = Dog("lucy",3)
lucy.sit()
lucy.roll_over()