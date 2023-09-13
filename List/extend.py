list1 = [1,3,5,7,9]
print("this is list1",list1)

list2 = [0,2,4,6,8]
print("this is list2", list2)

list1.extend(list2)
list2.extend(list1)

print("combine list",list1)

print("combine list", list2)