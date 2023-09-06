class Laptop:
    def __init__(self, brand, release_year, color, RAM):
        self.brand = brand
        self.release_year = release_year
        self.color = color
        self.RAM = RAM

    def coding(self):
        print("Coding in progress...")
        # self.RAM -= 1
        self.RAM -= 1
        print(self.brand + " is on coding process" )
        print("Remaining RAM : " + str(self.RAM))

class GamingLaptop(Laptop):
    def __init__(self, brand, release_year, color, RAM, VGA):
        super().__init__(brand, release_year, color, RAM)
        self.VGA = VGA

laptop_1 = Laptop("Macbook", "2022", "Space Grey", 8)
laptop_2 = Laptop("Dell", "2021", "Black", 16)
laptop_3 = Laptop("HP", "2020", "Silver", 32)
laptop_4 = Laptop("Lenovo", "2019", "White", 64)
laptop_5 = GamingLaptop("HP", "2020", "Silver", 64, "RTX 4060")


print(laptop_5.VGA)


# print(laptop_1.brand)
# laptop_1.coding()
# laptop_2.coding()
# laptop_3.coding()
# laptop_4.coding()

