class student:
    def __init__(self,name,id,mark):
        self.name=name
        self.id=id
        self.mark=mark
    def wellcome(self): #method
        print("bangladesh")
    def get_marks(self):
        return self.mark
s1=student('rakib',26,87)
print(s1.name)
print(s1.id)
print(s1.mark)


s1.wellcome() #call method
print(s1.get_marks())
