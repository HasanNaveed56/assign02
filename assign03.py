# Question 1

class Students:
    def __init__(self,name,age,roll_num=None):
        self.name = name
        self.age = age
        self.roll_num = roll_num
        self.__marks = 0

    def get__marks(self):
        return self.__marks
    
    def set__marks(self,marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks. Please enter a value between 0 and 100.")

    

   

s1 = Students(input("Enter student name: "), int(input("Enter student age: ")), input("Enter student roll number: "))

print("Name:", s1.name)  
print("Age:", s1.age)    

s1.set__marks(85)



print("Marks:", s1.get__marks())  
print("Roll Number:", s1.roll_num)  

# Question 2

class Person:   #parent class
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person): #single inheritance
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks = marks

class Moniter(Student): #multilevel inheritance
   
   pass

class Sports(Student): #multiple inheritance
    pass

class AllRounder(Moniter,Sports):  #multiple inheritance
    pass

class Teacher(Person): #hierarchical inheritance
    pass

class Principal(Person): #hierarchical inheritance
    pass

# Question 3

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

print ("list of strings", len("Hello, World!"))
print ("list of integers", len([1, 2, 3, 4, 5]))

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self):
        return self.value + self.value
    
class Cat(Animal):
    def sound(self):
        print("Cat meows")

a = Animal()
d = Dog()

a.sound()
d.sound()


n1 = (int(input("Enter first number: ")))
n2 = (int(input("Enter second number: ")))

print("Sum : ", n1 + n2)

c = Cat()
c.sound()