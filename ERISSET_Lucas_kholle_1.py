#! /bin/usr/env python3

# import
import sys, csv, argparse

# command argument
parser = argparse.ArgumentParser()
parser.add_argument("-l", help="Show all items from the list", action="store_true")
parser.add_argument("-a", help="Add item.s to the list", nargs="+")
parser.add_argument("-c", help="Remove all items from the list", action="store_true")
parser.add_argument("-s", help="Make some arithmetic functionality. Need --max, --min, --moy, --sum after it to work", action="store_true")
parser.add_argument("--max", help="Return max value of list (only work with -s command)", action="store_true")
parser.add_argument("--min", help="Return min value of list (only work with -s command)", action="store_true")
parser.add_argument("--moy", help="Return the average of list (only work with -s command)", action="store_true")
parser.add_argument("--sum", help="Return sum of list values (only work with -s command)", action="store_true")
parser.add_argument("-t", help="Sort list by ascending order and rewrite in file the sorted informations, add --desc for descending order", action="store_true")
parser.add_argument("--desc", help="Sort list in descending order, only work with -t command", action="store_true")

args = parser.parse_args()
# function

# read csv file function
def readFile():
    output = []
    tmpIntConverter = []
    path = input("Entrez le chemin du fichier csv : ")

    with open(path, 'r') as filename:
        reader = csv.reader(filename)
        for row in reader:
            tmpIntConverter += row

        for item in tmpIntConverter:
            item = int(item)
            output.append(item)
            
    return output

# add row in csv file function
def appendInFile(content):
    path = input("Entrez le chemin du fichier csv : ")

    with open(path, 'a', newline='') as filename:
        writer = csv.writer(filename)
        writer.writerow(content)

# write in csv file function
def WriteInFile(content):
    path = input("Entrez le chemin du fichier csv : ")

    with open(path, 'w', newline='') as filename:
        writer = csv.writer(filename)
        writer.writerow(content)

# delete row in csv file function
def deleteAllItems():
    path = input("Entrez le chemin du fichier csv : ")

    with open(path, 'r') as readFile, open(path, 'w') as writeFile:
        reader = csv.reader(readFile)
        writer = csv.writer(writeFile)
        for row in reader:
            writer.writerow(row[0:])

# command function

# -l show all items from the list
if sys.argv[1] == '-l':
    data = readFile()
    print(data)
    print("Action succesfuly achieve")
    
# -a [item1, item2, ...] add item to the list
elif sys.argv[1] == '-a':
    arguments = sys.argv[2:]
    appendInFile(arguments)
    print("Action succesfuly achieve")

# -c remove all items from the list
elif sys.argv[1] == '-c':
    deleteAllItems()
    print("Action succesfuly achieve")

# -s is use with --max, --min, --moy, --sum
elif sys.argv[1] == '-s':
    if len(sys.argv) < 3:
        print('Error: missing argument --max, --min, --moy, --sum after -s command')
# -s --max show max value from the list
    elif sys.argv[2] == '--max':
        data = readFile()
        print("Max value is : " + max(data))
# -s --min show min value from the list
    elif sys.argv[2] == '--min':
        data = readFile()
        print("Min value is : " + min(data))
# -s --moy show average from the list
    elif sys.argv[2] == '--moy':
        data = readFile()
        items = 0
        for item in data:
            items += int(item)
        print("Avg value is : " + items/len(data))
# -s --sum show sum from the list
    elif sys.argv[2] == '--sum':
        data = readFile()
        items = 0
        for item in data:
            items += int(item)
        print("Sum value is : " + items)

# -t --desc sorts the list in descending order
elif sys.argv[1] == '-t' and sys.argv[2] == '--desc':
        data = readFile()
        data.sort()
        data.reverse()
        WriteInFile(data)    
        print("Action successfuly achieve")
# -t sorts the list in ascending order
elif sys.argv[1] == '-t':
    data = readFile()
    data.sort()
    WriteInFile(data)
    print("Action successfuly achieve")
