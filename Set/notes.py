# element should be unique, cannnot be duplicate
# {}
# it can contain any element but that element should not be mutable. like list or dictionaries
# set has no particular order, means order is not preserved
# {} -> empty curly braces will make an empty dictionary in python
# to make a set without an elements, we use the set() function without any argument.

empty_set = set()

#create empty dictionary
empty_dictionary = {}

# sets are mutuable, if we want to add and update set items in python
# add()
# update()
# discard()  to remove an emelemt from set

# built in functions in sets

'''
all()       > Returns True if all elements of the set are true (or if the set is empty)
any()       > Returns True if any element of the set is true. If the set is empty, returns False
enumerate() > Returns an enumerate object. It contains the index and value for all the items of the set as a pair.
len()       > Returns the length (the number of items) in the set.
max()       > Returns the largest item in the set.
min()       > Returns the smallest item in the set.
sorte()     > Returns a new sorted list from elements in the set(does not sort the set itself).
sum()       > Returns the sum of all elements in the set.
'''


'''
Method	Description
add()                           > Adds an element to the set
clear()                         > Removes all elements from the set
copy()                          > Returns a copy of the set
difference()                    > Returns the difference of two or more sets as a new set
difference_update()	            > Removes all elements of another set from this set
discard()	                    > Removes an element from the set if it is a member. (Do nothing if the element is not in set)
intersection()	                > Returns the intersection of two sets as a new set
intersection_update()	        > Updates the set with the intersection of itself and another
isdisjoint()	                > Returns True if two sets have a null intersection
issubset()	                    > Returns True if another set contains this set
issuperset()	                > Returns True if this set contains another set
pop()	                        > Removes and returns an arbitrary set element. Raises KeyError if the set is empty
remove()	                    > Removes an element from the set. If the element is not a member, raises a KeyError
symmetric_difference()	        > Returns the symmetric difference of two sets as a new set
symmetric_difference_update()	> Updates a set with the symmetric difference of itself and another
union()	                        > Returns the union of sets in a new set
update()	                    > Updates the set with the union of itself and others
'''