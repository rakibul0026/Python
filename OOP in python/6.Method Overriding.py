class phone:
    def call(self):
        print("You can call")
    def message(self):
        print("you can message")
class vivo(phone):
    def call(self):
        print("this is call section")
        super().call()
    def photo(self):
        print("You can photo")

ob=vivo()
ob.call()
ob.photo()
ob.message()
