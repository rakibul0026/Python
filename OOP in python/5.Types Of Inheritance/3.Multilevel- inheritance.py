class phone:
    def call(self):
        print("You can call")
    def message(self):
        print("you can message")
class vivo(phone): # single Inheritance
    def photo(self):
        print("You can photo")
class samsung(vivo): #Multilevel inheritance
    def google(self):
        print("you can google search")


ob=samsung()
ob.call()
ob.photo()
ob.message()
ob.google()
