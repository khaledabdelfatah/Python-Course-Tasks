#Write a python script the user will enter a file name and you are required to read that file and print the number of words in it.

# filename = input("Enter file name: ")
filename="file3.txt"
with open(filename, "r") as file:
    data = file.read()
    words = data.split()
    num_words = len(words)
    print("Number of words in the file:", num_words)
