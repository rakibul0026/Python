#5. Hybrid Inheritance
class Phone:
    def call(self):
        print("You can call")
    
    def message(self):
        print("You can message")

class Vivo(Phone):  # Single Inheritance
    def photo(self):
        print("You can take photos")

class Samsung(Vivo):  # Multilevel Inheritance
    def google(self):
        print("You can use Google search")

class iPhone(Samsung):  # Multilevel and Hybrid Inheritance
    def video(self):
        print("You can record videos")

# Create an object of the iPhone class
ob = iPhone()
ob.call()       # From Phone class
ob.message()    # From Phone class
ob.photo()      # From Vivo class
ob.google()     # From Samsung class
ob.video()      # From iPhone class
