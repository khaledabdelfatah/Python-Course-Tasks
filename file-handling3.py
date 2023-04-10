#Write a function in Python to count the number of lines from a text file "file1.txt" which is not starting with an alphabet "t".

def countlinesnotstartingwitht(file_name):
    count = 0
    with open(file_name, 'r') as f:
        for line in f:
            if line[0].lower() != 't':
                count += 1
    return count
x=countlinesnotstartingwitht("file1.txt")
print(x)