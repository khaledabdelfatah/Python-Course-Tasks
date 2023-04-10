#Write a function in Python to read the content from a text file "file1.txt" line by line and display the same on screen.

def read_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            print(line.strip())


read_file("file1.txt")
