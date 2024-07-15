my_dict = {"Alexey" : 1999, "Dima" : 2000  }
print(my_dict)
my_dict["Nastya"] = 2001
print(my_dict)
print(my_dict.get("Alexey"))
print(my_dict.get("Nastya"))
my_dict.update({"Vika" : 1990, "Miha" : 2002})
print(my_dict)
del my_dict["Alexey"]
print(my_dict)
my_set = {1,2,3,4,5,1,2,3}
print(my_set)
my_set = {1,2,3,2,1,3}
my_set =set(my_set)
print(my_set)
print(my_set.add(5))
print(my_set.add(6))
print(my_set)
print(my_set.discard(1))
print(my_set)