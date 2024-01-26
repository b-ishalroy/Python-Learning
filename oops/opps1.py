class student:
    def self_name(self,name):
        self.name=name
        return self.name
    

student_1=student()
student_1.self_name("Bishal")
print(student_1.name)

student_2=student()
student_2.self_name("Kimti")
print(student_2.name)



# Using classes finding area and perimeter of the rectangle 
class rectangle:
    def rectangle_name(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.height*self.width

    def perimeter(self):
        return 2*(self.height+self.width)

rectangle_1=rectangle()
rectangle_1.rectangle_name(5,9)    
print("The height of the rectangle is =",rectangle_1.height,end=" and ")    
print("The width of the rectangle is = ",rectangle_1.width)
print("The area of the rectangle is =",rectangle_1.area())
print("The perimeter of the rectangle is =",rectangle_1.perimeter())


    



