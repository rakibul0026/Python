#item access in a dictionary
employee={
    "name":"sifat Hassan",
    "skill":["python","java","c++"],
    "year_of_experience":4
}
print(employee["name"])
print(employee["skill"])
print(employee["year_of_experience"])
#print(employee["salary"])

#item access in a dictionary [use get() ]

#print(employee.get("salary"))

#Change(1) item in a dictionary
#print(employee["name"])# before change
#employee["name"]="Test user"
#print(employee["name"])# after change

#change approch(2)->use .update ()
employee.update(
    
    {
        "name":"Text User",
        "year_of_experience":8
        
    }
)
print(employee)



