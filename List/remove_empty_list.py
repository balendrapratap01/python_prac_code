# solving this problem using list comprehension

list1 = [1,2,[],5,[],[],98]
print("The original list is: " + str(list1))


result = [element for element in list1 if element != []]

print(result)

# using filter() function

# filter() function we use to filter something from list.

list2 = [1,2,[],[],12,[],14]

result2 = list(filter(None,list2))

print(result2)

# using self made fucntion

def working_function(list3):
    new_list = []
    for element in list3:
        if element:
            new_list.append(element)
    return new_list

list3 = [1,2,[],12,[],[],[],1212,[]]
print(working_function(list3))
