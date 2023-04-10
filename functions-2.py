#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters

def count_case(s):
    upper_count = 0
    lower_count = 0
    
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    return upper_count, lower_count

text = "Hello, World!, AWS reStart"
upper_count, lower_count = count_case(text)
print("Number of upper case letters:", upper_count)
print("Number of lower case letters:", lower_count)
