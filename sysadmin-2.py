#write python script to create new file newfile in newdir directory then change file permission to be executable file.

import os

# Create a new directory called "newdir"
os.mkdir("newdir")

# Create a new file called "newfile" in the "newdir" directory
with open("newdir/newfile", "w") as f:
    f.write("This is a new file.")

os.chmod("newdir/newfile", 0o755)
