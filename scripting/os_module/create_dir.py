import os

# Directory
directory = "test_dir"

# Parent directory
parent_directory = "C:/Users/Shafi/Documents"

# Path
path = os.path.join(parent_directory, directory)

# Create Dir
os.mkdir(path)
