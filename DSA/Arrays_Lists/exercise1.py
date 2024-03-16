# this exercise is provided by codebasics on YT
# * URL of the exercise - https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md 

expense = [2200,2350,2600,2130,2190]

extra_in_feb = expense[1] - expense[0]
print(extra_in_feb)
sum = 0
for i in range(0,3):
    sum += expense[i]

print("The expense in first quater = " , sum)

# for i in range(5):
#     if(expense[i] == 2000):
#         print("2K Dollars spent in ",i)
#     else:
#         print("exact 2k dollars not spent in ",i)

# * Alternate for this 2k dollar check question :

if(2000 not in expense):
    print("Exact 2k dollar not spent in any month")


expense.insert(7,1980)
print("List after June month expense :" , expense)
# * Alternate is using append() function
print(expense.index(1980))
expense.append(2000)
print("List after July Month expense :", expense)

expense[3] -= 200

print("List after refund in April Month : ", expense)

