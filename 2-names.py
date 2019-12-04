#Use Intention-Revealing Names

d = 0 #Time Elapsed in days
#If a name requires a comment, then the name does not reveal its intent
elapsedTimeInDays = 0
daysSinceCreation = 0
daysSinceModfication = 0
fileAgeInDays = 0
#-----------------------------------------------------------------------

#What is the purpouse of this code?

def getThem(list):
    list1 = []
    for i in list:
        if i[0] == 4:
            list1.append(i)
    return list1

#Good names reveal purpouse

def getFlaggedCells(gameBoard):
    flaggedCells = []
    for cell in gameBoard:
        if cell['status'] == 'flagged':
            flaggedCells.append(cell)
    return flaggedCells

#Creating a method for the if condition
def getFlaggedCells(gameBoard):
    flaggedCells = []
    for cell in gameBoard:
        if cell.isFlagged():
            flaggedCells.append(cell)
    return flaggedCells
#-----------------------------------------
#Avoid missinformation.

def copyChars(a1,a2):
    for i in a1:
        a2[i] = a1[i]
    return a2

def copyChars(source,destination):
    for i in source:
        destination[i] = source[i]
    return destination

