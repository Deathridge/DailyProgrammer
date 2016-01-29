from tabulate import tabulate

text = []
while True:
    input_text = input()
    if input_text.strip() == "":
        break
    text.append(input_text)
    
column = []
row = []
isColumn = True
for item in text:
    if item == '-':
        isColumn = False
    if isColumn:    
        column.append(item.split())
    else:    
        row.append(item.split())
        
row = row[1::]

 
def columnSummer(column):
    columnSum = [0 for x in range(0, len(column[0]))]
    for rowNum in range(0, len(column[0])):
        for columnNum in range(0, len(column)):        
            columnSum[rowNum] += int(column[columnNum][rowNum])

    return columnSum

def rowSummer(row):
    rowSum = [0 for x in range(0, len(row))]
    for rowNum in range(0, len(row)):
        for columnNum in range(0, len(row[rowNum])):        
            rowSum[rowNum] += int(row[rowNum][columnNum])

    return rowSum

def fullRows(row):
    fullRows = []
    sumRow = rowSummer(row)
    sumColumn = columnSummer(column)
    for row in range(0, len(sumRow)):
        if sumRow[row] == len(sumColumn):
            fullRows.append(row)
    return fullRows

def fullColumns(column):
    fullColumns = []
    sumRow = rowSummer(row)
    sumColumn = columnSummer(column)
    for column in range(0, len(sumColumn)):
        if sumColumn[column] == len(sumRow):
            fullColumns.append(column)
    return fullColumns


def solver(row, column):
    solutionGrid = [[0 for x in range(0, len(row))] for x in range(0, len(column[0]))]
    sumColumn = columnSummer(column)
    sumRow = rowSummer(row)  

    fullColumn = fullColumns(column)
    fullRow = fullRows(row)

    for column in fullColumn:
        for rowNum in range(0, len(row)):
            print(rowNum,column)
            solutionGrid[rowNum][column] = '*'

    for row in fullRow:
        for colNum in range(0, len(column[0])):
            solutionGrid[row][colNum] = '*'
        
    print(fullColumn)
    print(fullRow)
    print(tabulate(solutionGrid))


solver(row,column)
