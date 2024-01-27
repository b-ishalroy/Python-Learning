# create a bus child that inherits from the vehicle class.the default fare charge of any vehicle is seating capacity * 100. if the vehicle is bus instance, we need to add an extra 10% on full fare as a maintainance charge. so total fare for bus instance will become the final amount = total amount + 10% pf the total fare  


class Vehicle:
    def __init__(self,seating_capacity):
        self.seating_capacity=seating_capacity

    def get_fare(self):
        return self.seating_capacity*100

class Bus(Vehicle):
    def __init__(self,seating_capacity):
        super().__init__(seating_capacity)  

    def get_fare(self):
        vehicle_fare=super().get_fare()
        maintainance_fare=0.1*vehicle_fare
        total_fare=vehicle_fare+maintainance_fare
        return total_fare

vehicle_1=Vehicle(99)     
print("The fare of the vehicle is =",vehicle_1.get_fare())

bus_1=Bus(199)
print("The fare of the Bus is=",bus_1.get_fare())



   


class Animal:
    def speaks(self):
        pass

class Dog(Animal):
    def speaks(self):
        print("Barks")

class Cat(Animal):
    def speaks(self):
        print("meow")            

Dog().speaks()
Cat().speaks()










   