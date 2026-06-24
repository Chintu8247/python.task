# Base Class
class Vehicle:
    def __init__(self, color, max_speed, brand):
        self.__color = color      # Private attribute (Encapsulation)
        self.max_speed = max_speed
        self.brand = brand

    # Getter method
    def get_color(self):
        return self.__color

    # Setter method
    def set_color(self, color):
        self.__color = color

    def start_engine(self):
        print(f"{self.brand} vehicle engine started.")

    def stop_engine(self):
        print(f"{self.brand} vehicle engine stopped.")


# Subclass
class Car(Vehicle):
    def __init__(self, color, max_speed, brand, num_doors, transmission_type):
        super().__init__(color, max_speed, brand)
        self.num_doors = num_doors
        self.transmission_type = transmission_type

    # Polymorphism (Method Overriding)
    def start_engine(self):
        print(f"{self.brand} car engine started with a push-button start!")

    def lock_doors(self):
        print("Doors are locked.")

    def unlock_doors(self):
        print("Doors are unlocked.")


# Creating Vehicle Objects
vehicle1 = Vehicle("Red", 180, "Toyota")
vehicle2 = Vehicle("Blue", 200, "Honda")

# Creating Car Object
car1 = Car("Black", 240, "BMW", 4, "Automatic")

# Encapsulation Demo
print("Original Color:", car1.get_color())
car1.set_color("White")
print("Updated Color:", car1.get_color())

# Car Methods
print("\nCar Details:")
print("Brand:", car1.brand)
print("Max Speed:", car1.max_speed)
print("Doors:", car1.num_doors)
print("Transmission:", car1.transmission_type)

car1.start_engine()
car1.lock_doors()
car1.unlock_doors()
car1.stop_engine()

# Abstraction Demo using List of Vehicles
print("\nVehicle Operations:")
vehicles = [vehicle1, vehicle2, car1]

for vehicle in vehicles:
    vehicle.start_engine()
    vehicle.stop_engine()
    print("-" * 30)