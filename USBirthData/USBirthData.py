
##### Import Libraries Section #####
import pprint 
from collections import defaultdict

##### Functions Declaration Section #####

#Function takes in raw data, eliminates empty row(s) and header 
def filterRows(rawData):
    #Get Rows/Data in a list
    rows = rawData.split('\n')
    filteredData = []
    for row in rows:
        #join - takes care of empty rows like ',,,,,,,'
        if (''.join(row.split(',')).strip() != '') and row:
            # If Row is NOT empty
            #Split each Row into columns and create a new list
            ln = row.split(",")
            filteredData.append(ln)
    
    # Remove the Header
    filteredData = filteredData[1:len(filteredData)]
    return filteredData

def fnCalculateBirth(rec, dict):
    if rec[0] in dict:
        dictMonth = dict[rec[0]]
        if rec[1] in dictMonth:
            dictMonth[rec[1]] += int(rec[4])
        else:
            dictMonth[rec[1]] = int(rec[4])
        dict[rec[0]] = dictMonth
    else:
        dict[rec[0]] = {rec[1] : int(rec[4])}
    return dict


##### Variables Initialization #####
dictFriday = defaultdict(list)
dictWeekends = defaultdict(list)
##### Processing Section #####

# Read Data 
fopen = open("C:\\Personal\\USBirthData\\Data\\USBirthData.csv", "r")
data = fopen.read()

# Filter Data
arrFileContents = filterRows(data)

# For every row
for rec in arrFileContents:
    #### Num of Births on 13th Friday, Year  & Month
    # 0 Year, 1 Month, 2 Date Of Month, 3 Day Of Week, 4 Births
    # Data Structure: Dictionary [Year]:[[Month][Count]]
    if (int(rec[3]) == 5 and int(rec[2]) == 13):
        # For Key [Year], List of Values of [[Month][Count]]
        dictFriday = fnCalculateBirth(rec, dictFriday)
    #### Num of Births on Weekend Year  & Month
    # 0 Year, 1 Month, 2 Date Of Month, 3 Day Of Week, Births
    # Data Structure: Dictionary [Year]:[[Month][Count]]
    if (int(rec[3]) == 6 or int(rec[3]) == 7):
        # For Key [Year], List of Values of [[Month][Count]]
        dictWeekends = fnCalculateBirth(rec, dictWeekends)

print ("\n #### Num of Births on 13th Friday ##### ")
pprint.pprint(dictFriday)

print ("\n #### Num of Births on Weekends ##### ")
pprint.pprint(dictWeekends)