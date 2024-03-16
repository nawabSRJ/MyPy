name = "Srajan Saxena"

# ! Note - All these functions don't change the actual string

print(name.upper()) # * converts whole string to UPPER CASE

print(name.lower())  # * converts whole string to lower case

print(name.find('raj'))  # * Searches for a specified substring in the string and returns the lowest index.

print(name.capitalize()) # * Capitalizes only the first character of the complete string (Note - in case of a full name , surname's first word is not capitalized). ; aslo makes all other character as lower case

print(name.title())  # * Capitalizes the first character of each word in the string.

print("raj" in name)    # * using 'in' keyword to check for a substring in the string, returns True if found else returns False

print(name.swapcase()) # * Swaps the case of each character in the string.

print(name.strip()) # * Removes leading and trailing whitespace characters.

# * str.lstrip() :	Removes leading whitespace characters.

# * str.rstrip()	Removes trailing whitespace characters. 
newString = "Hey!!!!!"
print(newString.rstrip("!"))

# * Checks if the string starts with a specified value. (case sensitive)
print(name.startswith('S')) # * True
print(name.startswith('s')) # * False
print(name.startswith('Sra')) # * True
print(name.startswith('Srj')) # * False

# *Checks if the string ends with a specified value.
print(name.endswith('jan'))  # * False
print(name.endswith('ena'))  # * True

print(name.replace("sra" , "sar"))  # * no change - as "sra" is not found
print(name.replace("Sra" , "sar"))  # * replaced 
print(name.replace("Srajan" , "Aaditya"))  # * replaced 

print('Split Here\n\n\n')
lst = "Srajan 18 Male"
print(lst.split(" "))   # * Creates a list based on the separator passed

print(name.count("a")) # * no. of times a particular character is occuring

name2 = "AadityaAatreySaxena189"
print(name2.count("Aa")) # * also checks for substrings

name_new = "SrajanSaxena"
print(name_new.isalnum()) # *returns True if string is made of a-z , A-Z , 0-9 with no white space
print(name_new.isalpha()) # * returns True if No Numeric Character is there
print(name2.isalpha())
