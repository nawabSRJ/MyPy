cube30 = [x**3 for x in range(1,31)]
print(cube30)

def makecube(x):
    return x**3

num_list = [x for x in range(1,31)]
print(num_list)
cube_list = list(map(makecube , num_list))
print(cube_list)
print('\n')
print('\n')
if cube_list == cube30 :
    print('yassss')

