import os
import sorterfunctions
from uservarariables import FileLocation

# Directory where files to be moved from and destinations are. Use double \\ and end with double \\
files_to_sort = 'C:\\Users\\tommy.clarke\\Documents\\Bot\\Sorter\\TBS\\'


# Calls sort function to sort and move files based on filename
for file in os.listdir(files_to_sort):
    sorterfunctions.sort(file, files_to_sort)