import csv

def csvlist_to_list(csvname, delimiter=','):
    with open(csvname, 'r') as csvfile:
        return list(csv.reader(csvfile, delimiter=delimiter))[0]

def list_to_csvlist(mylist, csvname):
    with open(csvname, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)
        csvwriter.writerow(mylist)        
    
        