 #Multiple Inheritance
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
class iphone(samsung,vivo): # Multiple Inheritance
    def video(self):
        print("you can video in this")


ob=iphone()
ob.call()
ob.photo()
ob.message()
ob.google()
ob.video()
