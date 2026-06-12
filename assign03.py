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