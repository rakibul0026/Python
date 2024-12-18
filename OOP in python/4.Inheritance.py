class phone:
    def call(self):
        print("You can call")
    def message(self):
        print("you can message")
class vivo(phone): #Inheritance
    def photo(self):
        print("You can photo")

ob=vivo()
ob.call()
ob.photo()
ob.message()
