import math
alpha = {0:'Z',1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}


# taking'rem' variable as remainder

# # prefix -> math.floor(rem)
# if(rem <= 1):
#     ans = alpha[cn]
#     print(ans)
# else :   
#     prefix = alpha[math.floor(rem)]
#     postfix =  alpha[cn - (26 * math.floor(rem))] 
#     ans = prefix + postfix
#     print(ans)
 
cn = int(input("Enter the Column Number : \t"))

mod = cn % 26
if(mod == 0):
    cn -= 1        
rem = cn / 26      
if(rem <= 1):
    ans = alpha[cn]
    print(ans)
else:
    prefix = alpha[math.floor(rem)]
    
    postfix = alpha[mod]
    ans = prefix + postfix
    print(ans)
    






