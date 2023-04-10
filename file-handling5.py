# Open the file for reading and store its contents in a list
with open('file3.txt', 'r') as f:
    lines = f.readlines()

# Remove lines 3-6 from the list of lines
del lines[2:6]

# Open the file for writing and write the modified contents
with open('file3.txt', 'w') as f:
    f.writelines(lines)
