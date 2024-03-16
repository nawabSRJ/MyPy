old = ['a' ,'b','a','c' ,'b','a']

# * Naive Method :
# new = []
# for item in old :
#     if item not in new :
#         new.append(item)

# * One Liner Alternative
print(old.values())
new = list(dict.fromkeys(old).keys())
print(new)
