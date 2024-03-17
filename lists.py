# len(): to find length of a list.
l1=[1,"ved",True]
# print(l1)


l2=list(("devs","ram")) # using list constructor.
# print(l2)



if "devs" in l2:
     print("yes")



l2[0]="nidhis"
# print(l2)

l2.insert(1,"hello")
# print(l2)


l2.append("geeta")
l2.extend(l1)
# print(l2)


# clear ,pop, remove are the methods to delete but del is a keyword

l2.pop(0)
l2.remove("hello")
del l2[3]
# print(l2)

# l2.clear()
# print(l2)



# for x in l2:
#      print(x)



# print((x) for x in l2)


# list comprehension
     
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

l=[x for x in fruits if 'a' in x]
# print(l)


l=[x**2 for x in range(1,10)]
# print(l)

# print(fruits.index("cherry"))

fruits.reverse()
fruits.sort()
print(fruits)
l5=fruits.count("apple")
print(l5)