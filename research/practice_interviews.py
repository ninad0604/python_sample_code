from collections import Counter, OrderedDict, defaultdict


#String
s= "this is very long length of string."

print(s[::-1])
# .gnirts fo htgnel gnol yrev si siht

print(s+s)

print(s.count("l"))
print(s.index('i'))
print(s.find('g'))
print(s.rfind('g'))


# List

my_list = [1,5,6,64,67,69,58,9,4,4,52,6,51,4,6,57,45]
my_dict = {"4": 35,"rg": 35,"ffdbs": 35, "66": 35,"5t": 35,"35": 35,"45": 35,"bb": 35,"rh": 35,"55t": 35}
my_list.append(5)
print(my_list)
#c= Counter(my_list)
#print(c)
class OrderedCounter(Counter, OrderedDict):
    pass


oc = OrderedCounter(my_list)
for key, val in oc.items():
    print(key, val)

#search for key in dict:
if '4' in my_dict:
    pass

#search for val
if 35 in my_dict.values():
    pass

# search for key val pair:
#if key, val in my_dict.items():



# List traversal
print("List traversal")

# when we are only want to use values and operate on it, not trying to alter the list
for i in my_list:
    print(i)

# Using enumerate you get index as well you can use index to update values in list. Useful for some sorting and updating values

# CAUTION: Enumerate does not return index. It returns a counter, it only increases in steps and hence can't be used
# where you are working with indices, somewhere in the middle or jumping between indices.
for idx, val in enumerate(my_list):
    print(idx, val)

# here index starts at 1
#
for c, value in enumerate(my_list, 1):
    print(c, value)



# The following method is prefered in problems where the operations are made on list itself to alter/update any value.
for i in range(len(my_list)):
    print(i, my_list[i])


# range function is very useful and powerful
print(list(range(4,50,5)))
print(list(range(1,50,5)))
print(list(range(50,1,-1)))
print(list(range(39,4,-4)))
length= len(my_list)
print(list(range(length)))

print(list(range(40)))
for i in range(1,length+1):
    print(i)


##iterating over dict


