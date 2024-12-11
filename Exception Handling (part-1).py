try:
    list = [20, 0, 30]
    result = list[0] / list[3]  
    print(result)
except ZeroDivisionError:
    print("Dividing by zero is not possible.")
except IndexError:
    print("Index out of range.")
    print("DONE")
finally:
   print("wellcome to CSE Family in CSTU")

