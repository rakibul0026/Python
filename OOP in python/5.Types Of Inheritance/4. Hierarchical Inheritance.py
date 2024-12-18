4. Hierarchical Inheritance
class Phone:
    def call(self):
        print("You can call")
    def message(self):
        print("You can message")

class Vivo(Phone):  # Hierarchical inheritance
    def photo(self):
        print("You can take photos with Vivo")

class Samsung(Phone):  # Hierarchical inheritance
    def google(self):
        print("You can perform Google searches with Samsung")

# Create objects of Vivo and Samsung
vivo_phone = Vivo()
samsung_phone = Samsung()

# Vivo phone functionalities
vivo_phone.call()
vivo_phone.message()
vivo_phone.photo()

print()

# Samsung phone functionalities
samsung_phone.call()
samsung_phone.message()
samsung_phone.google()
