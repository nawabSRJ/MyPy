rows = int(input('Enter rows : '))
c = 1
p = 1
for i in range(1,rows+1):
    print((rows-p) * " ",end="")
    print(c * "*")
    c += 2
    p += 1
