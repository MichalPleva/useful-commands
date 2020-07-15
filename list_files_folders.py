import glob

path = 'path_to_files/'

#List all .txt files in a specified directory + subdirectories (**).
files = [f for f in glob.glob(path + "**/*.txt", recursive=True)]

# List all directories in a specified directory + subdirectories (**).
folders = [f for f in glob.glob(path + "**/", recursive=True)]
