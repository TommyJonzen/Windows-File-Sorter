# Windows-File-Sorter
Sorts files on a Windows system from one directory to many directories based on filenames. Will also delete any duplicates found.
It is a good idea to first create a copy of the folder you are going to be sorting. This script will move your files rather than copy, so if you input an incorrect
or non existant file path as the destination folder then you could lose your files!

## Requirements
- An installation of python3
- A machine running Windows

## How to Use
In your terminal navigate to where you would like to store this script and clone it.

There are two important files in this repo that will require some customisation for your needs:
- file-sort.py
- sorterfunctions.py

### Customising file-sort.py

- Open file-sort.py in your favourite text editor. After the import calls at the top of the file you will see the below:

```Directory containing files to be moved. Use double \\ and end with double \\
files_to_sort = 'C:\\Users\\user.name\\Documents\\files\\stuff\\'
```

- Edit the filepath for the variable 'files_to_sort' to be the filepath for the directory containing the files you want sorted. 

Please note that due to how python interprets the backslash character you need to use double '\\\\' in all instances where you are inputting filepaths.
Additionally for the purposes of this script you need to end all filepaths with a double \\\\.

eg. if your files were stored at <b>C:\Users\liam.n\documents\mystuff</b>
Then you should edit the line to look like:
```
files_to_sort = 'C:\\Users\\liam.n\\documents\\mystuff\\'
```

That's all that is required in file-sort.py!


### Customising sorterfunctions.py

- Open sorterfunctions.py in your favourite text editor

Inside this file there are two functions, the first is called 'move' <b>which you do not need to touch at all</b>.
Instead find the second function on the page called 'sort' (line 59 where it says: 'def sort(filename, location_to_sort_from)')

You will need to edit the if statements within this sort function to suit your own situation. When you open the file it will look like:

```# All conditions for moving files to appropriate directory
   if 'delivery' in filename:
       destination = 'C:\\Users\\user.name\\Documents\\delivery-reports\\'

   elif 'notification' in filename:
       destination = 'C:\\Users\\user.name\\Documents\\Sales-Notes\\'

   else:
       return
```

Note that the filepaths contain double \\\\ as separators and end with a double \\\\. This is important.


In the sort function the only thing you need to edit are the 'if' and 'elif' statements (you can add as many elif statements as you like), do not edit the else statement.

This script works by matching patterns you give in the if statements to the file names in the folder you want sorted. You can see in the example above if the word 'delivery'
is in the file name the script knows to move the file from the sort folder to a new destination 'C:\\Users\\user.name\\Documents\\delivery-reports\\'

##### Say you have 3 types of files in your sort folder:
- Stock Report PDFs (stockreport1.pdf, stockreport2.pdf, stockreport3.pdf, etc.)
- Order PDFs (order1.pdf, order2.pdf, order3.pdf, etc.) 
- Stock Spreadsheets (stock1.xlsx, stock2.xlsx, stock3.xlsx)

- You want Stock Report PDFs moved to: C:\\Users\\user.name\\Documents\\stockpdfs\\
- You want Order PDFs moved to: C:\\Users\\user.name\\Documents\\orderpdfs\\
- You want Stock Spreadsheets moved to: C:\\Users\\user.name\\Documents\\stocksheets\\

Your 'sort' function if statements could then look like:

``` # All conditions for moving files to appropriate directory
    if 'stockreport' in filename:
        destination = 'C:\\Users\\user.name\\Documents\\stockpdfs\\'

    elif 'order' in filename:
        destination = 'C:\\Users\\user.name\\Documents\\orderpdfs\\'
        
    elif 'xlsx' in filename:
        destination = 'C:\\Users\\user.name\\Documents\\stocksheets\\'   

    else:
        return
```

Now all three file types will be sorted on their unique attributes into the chosen destination folders. 

Take particular note of the second elif statement: <b>elif 'xlsx' in filename:</b>
We couldn't look for the word stock in stock.xlsx files as that would also try to sort stockreport.pdf files.
However we only have one of this file type in the folder so we can just sort it based on the file extension 'xlsx'.

If you had more than one type of this file type in your folder to be sorted. Say you also had monthly financial spreadsheets (aprilfinance.xlsx) 
then you could use 'and' statements:

``` 
   elif 'xlsx' and 'stock' in filename:
        destination = 'C:\\Users\\user.name\\Documents\\stocksheets\\'   
```

You can make these if statements as simple or as complex as you like based on your comfort with Python! Just make sure you make a copy of your 
to be sorted folder before you do any sorting in case you make a mistake. Alternatively you can create a test folder to fine tune the script to your needs
before having it sort your 'tenyearsofdownloadsandstuff' folder.

### Using After Customising
Now you have edited the scripts to work with your particular needs you can run it in your terminal.

- Make sure you are in the directory where you have saved the script and enter the following
- python file-sort.py

That's it! Your files will now be sorted. You can save multiple edited versions of this script for different scenarios of sorting. 
Or if you have a folder that regularly needs sorting you can run this script in windows task scheduler to do it for you.
