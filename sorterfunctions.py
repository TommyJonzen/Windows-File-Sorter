import shutil
import os
import datetime


# IGNORE THIS FUNCTION
# Function to move files from source directory to the destination directory defined in sort function
def move(filename, location_to_sort_from, destination):

    src_file = os.path.join(location_to_sort_from, filename)  # Path to actual file currently
    created_time_src = os.path.getctime(src_file)  # Time the file was created

    # Checks if filename already exists in destination directory - if not then moves file
    if not os.path.isfile(destination + filename):
        shutil.move(src_file, destination)
        print(filename, 'moved to', destination)

    # If filename does already exist in destination directory
    else:
        # Created time of the file with same filename in destination directory
        created_time_dest = os.path.getctime(destination + filename)

        # Checks if created times are the same - if so delete file in source dir without moving
        if created_time_dest == created_time_src:
            if os.path.getsize(src_file) == os.path.getsize(destination + filename):
                os.remove(src_file)
                print(filename + "was duplicate: Deleted")

            # If filenames and created times are the same but size is different
            else:
                # Create variable for src_file size and append to filename
                src_size = os.path.getsize(src_file)
                filename = src_size + "bytes_" + filename
                new_file_path = os.path.join(location_to_sort_from + filename)
                os.rename(src_file, new_file_path)

                # Recursively call move on newly created filename to check that also is not a duplicate
                move(filename, location_to_sort_from, destination)

        # If filenames are the same but created times are different
        else:
            # Variable for hours mins and secs of created time of source file
            src_hour_min_sec = datetime.datetime.fromtimestamp(created_time_src).strftime('%H:%M:%S')

            # Replace ':' in variable which is not allowed in windows filenames
            src_hour_min_sec = src_hour_min_sec.replace(':', '')

            # Rename file in source directory by adding created time
            filename = src_hour_min_sec + "_" + filename
            new_file_path = os.path.join(location_to_sort_from + filename)
            os.rename(src_file, new_file_path)

            # Recursively call move on newly created filename to check that also is not a duplicate
            move(filename, location_to_sort_from, destination)


# Edit sort if statements to your needs
# Sorts files into correct directory based on filename
def sort(filename, location_to_sort_from):

    # All conditions for moving files to appropriate directory
    if 'delivery' in filename:
        destination = 'C:\\Users\\user.name\\Documents\\delivery-reports\\'

    elif 'notification' in filename:
        destination = 'C:\\Users\\user.name\\Documents\\Sales-Notes\\'

    else:
        return

    move(filename, location_to_sort_from, destination)
