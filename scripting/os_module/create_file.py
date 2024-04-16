import os

# Directory
directory = "test_dir"

# Parent directory
parent_directory = "C:/Users/Shafi/Documents"

# Path
path = os.path.join(parent_directory, directory)

# Filename
filename = "testfile.txt"

# Filepath
filepath = os.path.join(path, filename)

# Create the file
with open(filepath, "w") as file1:
    toFile = "Contents of the file go here!"
    file1.write(toFile)
print(f"File {filename} created in {directory} folder!")