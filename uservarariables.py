# Enter filepath for where files are to be sorted from
# Replace path between quotes with your own path, use double \\
source_dir = "C:\\Users\\my.user\\files"




class FileLocation:
    def __init__(self, src, destination):
        self.src = src
        self.destination = destination