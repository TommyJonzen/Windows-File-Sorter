import os
import sorterfunctions

# Directory where files to be moved from and destinations are. Use double \\ and end with double \\
files_to_sort = 'C:\\Users\\user.name\\Documents\\files\\stuff\\'


# Calls sort function to sort and move files based on filename
for file in os.listdir(files_to_sort):
    sorterfunctions.sort(file, files_to_sort)