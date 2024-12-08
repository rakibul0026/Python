matrix=[
    [1,2,3],
    [4,5,6],

]
#edit matrix
matrix[0][1]=12
print(matrix[0][1])

#print matrix using for loop
print("The Matrix Element Are:")
for row in matrix:
    for element in row:
       print(element)
