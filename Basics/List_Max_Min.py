seq = [3,5,45,65,12,32,34,92,88,1]

maximum = seq[0]
minimum = seq[0]
for i in seq:
    if(seq[i]>maximum):
        maximum = seq[i]
    
for j in seq:
    if(seq[i]<minimum):
        minimum = seq[i]

print("Maximum Element = ",maximum ,"\nMinimum Element =",minimum)
