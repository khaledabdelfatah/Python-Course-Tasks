#write python script create 5 files take there name from user.



for i in range(5):
    filename = input("Enter file name: ")
    with open(filename, 'w') as f:
        f.write("This is a sample file.")
    print(f"{filename} created successfully!")
