#Chapter 2: Meaningful Names

#-------------------------------

#Use Intention-Revealing Names

d = 0

#vs

elapsedTimeInDays = 0
daysSinceCreation = 0
daysSinceModification = 0
fileAgeInDays = 0

#Not only for variables but for the whole code.
#Code should be explicit

def getThem():
    list1 = 1
    for x in theList:
        if x[0] == 4:
            list1.add(x)
    return list1

#vs

def getFlaggedCells():
    flaggedCells = []
    for cell in gameboard:
        if cell['STATUS_VALUE'] == 'FLAGGED':
            flaggedCells.add(cell)
    return flaggedCells

#Or even better:
#Writting a simple class instead of using and array of ints and using methods in conditional statements

def getFlaggedCells():
    flaggedCells = [] #If this were Java it would be an array of objects instead of integer
    for cell in gameboard:
        if cell.isFlagged():
            flaggedCells.add(cell)
    return flaggedCells

#-------------------------------

#Avoid Disinformation

#Example: Do not refer to a grouping of accounts as accountList unless it's actually a List

accountList = (acc1,acc2,acc3) #Wrong

#vs

accountList = [acc1,acc2,acc3] #Correct

#Or use

accounts = [acc1,acc2,acc3]

#-------------------------------

#Make meaningful distinctions

def copyChars(a1,a2):
    for i in len(a1):
        a2[i] = a1[i]

#vs

def copyChars(source,destination):
    for char in len(source):
        destination[char] = source[char]

#-------------------------------

#Use Pronounceable Names

class DtaRcrd102:
    def __init__(self):
        self.genymdhms = None
        self.modymdhms = None
        self.pszqint = "102"

#vs

class Customer:
    def __init__(self):
        self.generationTimestamp = None
        self.modificationTimestamp = None
        self.recordId = "102"

#-------------------------------

#Use Searchable Names
#Tip: The length of a name should correspond to the size of its scope

for i in range(34):
    s += (t[j]*4)/5

#vs

realDaysPerIdealDay = 4
WORK_DAYS_PER_WEEK = 5
sum = 0
for i in NUMBER_OF_TASKS:
    realTaskDays = taskEstimate[i] * realDaysPerIdealDay
    realsTaskWeeks = (realdays / WORK_DAYS_PER_WEEK)
    sum += realTaskWeeks

#-------------------------------

#Class names should have noun or noun phrase names

class Customer:
    pass

class AddressParser:
    pass

#Method names should be verbs or verb phrases

def setName():
    pass

def doSomething():
    pass

#-------------------------------

#Final example

#Variables with unclear context:

def printGuessStatistics(candidate, count):
    number = ""
    verb = ""
    pluralModifier = ""
    if count == 0:
        number = "no"
        verb = "are"
        pluralModifier = "s"
    elif count == 1:
        number = "1"
        verb = "is"
        pluralModifier = ""
    else:
        number = str(count)
        verb = "are"
        pluralModifier = "s"
    guessMessage = f"There {verb} {number} {candidate}{pluralModifier}"
    print(guessMessage) 

#vs

#Variables have a context

class GuessStatisticsMessage:
    def __init__(self):
        self.number = ""
        self.verb = ""
        self.pluralModifier = ""

    def makeString(candidate, count):
        createPluralDependentMessageParts(count)
        return f"There {self.verb} {self.number} {candidate}{self.pluralModifier}"

    def createPluralDependentMessageParts(count):
        if count == 0:
            thereAreNoLetters()
        elif count == 1:
            thereIsOneLetter()
        else:
            thereAreManyLetters(count)

    def thereAreManyLetters(count):
        number = str(count)
        verb = "are"
        pluralModifier = "s"

    def thereIsOneLetter():
        number = "1"
        verb = "is"
        pluralModifier = ""

    def thereAreNoLetters():
        number = "no"
        verb = "are"
        pluralModifier = "s"

