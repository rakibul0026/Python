#String and String Slicing in python
string="We all love our country"
print(len(string))
print(string[1])
print(string[0:5]) # it also print 0 to 5 string
print(string[-1]) #it also print End 

print(string.endswith("country")) #check that the last string is country if last string is country print 
print(string.endswith("our"))

print(string.count("a"))

print(string.capitalize())# only first string capital
print(string.upper()) #All  string capital

print(string.replace("country","motherland"))
print(string.find("all"))
