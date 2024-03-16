
# Batham Code

mycode = '''Program to print the lowest and 2nd lowest number in Python'''

nums = []

for i in range(5):
    elt = int(input("Enter Number : "))
    nums.append(elt)


min1 = min2 = nums[0]

for j in range(len(nums)):
    if(min1 > nums[j]):
        min1 = nums[j]

for j in range(len(nums)):
    if(min2 > nums[j] and nums[j] != min1):
        min2 = nums[j]

print(min1)
print(min2)
