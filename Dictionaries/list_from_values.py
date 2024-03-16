d1 = {1:3 , 2:2, 3:1 , 4:2}
# todo - to make list out of d1 dict values
ocuur_list = list(d1.values())
print("List of occurences of values ->",ocuur_list)   
uni_ocr = list(dict.fromkeys(ocuur_list).keys())

print("Unique Occurence values ->",uni_ocr)

if len(ocuur_list) == len(uni_ocr):
    print('Yes')
else:
    print(False)

# print(len(d1.values()) == ) 