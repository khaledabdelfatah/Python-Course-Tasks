def count_vowels(word):
    vowels = "AEIOUaeiou"  
    count = 0 
    for letter in word:
        if letter in vowels:
            count += 1
    return count

word="AEIOUkhaled"
print(f" Number of vowels are in {word} " +str(count_vowels(word)))
##############################################################################################
def hiddencardquiz(cardnum):
    cardlength= len(cardnum) - 4
    last_four = cardnum[-4:]
    # Replace all other digits with asterisks
    return( "*" * cardlength + last_four )
cardnumber="300012387478329"
print(f"your number that start with {cardnumber[0:4]} ends with "+hiddencardquiz(cardnumber))

############################################################################################

def doublechar(string):
    doubled = ""
    for char in string:
        doubled += char * 2
        print(doubled)
    return doubled

doublechar("now")

###########################################################################################

def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary
print(decimal_to_binary(10))
