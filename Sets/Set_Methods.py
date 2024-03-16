# * Set Methods and Operations

# todo - to change a set : 
# * add() : for adding one element 
# * update() : for adding a sequence

myset = {1,3}
myset.add(2)
myset.add(5)
print(myset)
l1 = [5,6,7]
myset.update(l1)
# ! in all cases, duplicates are ignored
print(myset)    
myset.update([4,5,6],[10,11,12],(14,15,16),{17,18,19,20})   # * can update with any type of sequence

print(myset)

# todo - remove element(s)
# * discard() - will remove an item if present
# *remove() - will remove an item if present, if not present then it will raise an exception

newset = {1,2,3,4,5,6}
newset.discard(69)
print(newset)

newset.remove(6)
print(newset)

# newset.remove(4)  # ! KeyError: 4

# * clear() - to remove all items from a set / to make a set empty
newset.clear()
print(newset)

# * returning / removing an item using pop() method - arbotrary removal of items
Newset = {11,20,3,12,15,17}
Newset.pop()
print(Newset)   # o/p : {2, 3, 17, 12, 15}
# 1 popped out 


