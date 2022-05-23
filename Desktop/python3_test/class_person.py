class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say_name(self):
        print("My name is : " +self.name)
    def say_age(self):
        print("My age is : " +self.age)

    def say_hello(self,target_name):
    	print("My name is : " +self.name+" , nice to meet you "+target_name)

person1 = Person("mardan","25")
person2 = Person("nadr","26")
person1.say_name()
person2.say_name()
person1.say_age()
person2.say_age()
person1.say_hello("mard")
#print(person1.age)
#print(person2.age)
#print(person1.name)
#print(person2.name)
print()


