picture = [[' ',' ',' ',' ','*'],
           [' ',' ',' ','*','*'],
           [' ',' ','*',' ','*'],
           [' ','*',' ',' ','*'],
           ['*','*','*','*','*']]

picture2 = [[' ',' ',' ',' ','*','*',' ','*',' ',' '],
            [' ',' ',' ','*','*','*','*','*',' ',' '],
            [' ',' ','*','*','*','*','*','*',' ',' '],
            [' ','*','*','*','*','*','*','*','*',' '],
            ['*','*','*','*','*','*','*','*','*','*'],
            [' ','*',' ',' ',' ',' ',' ',' ','*',' '],
            [' ','*',' ','*','*',' ','*',' ','*',' '],
            [' ','*',' ','*','*',' ','*',' ','*',' '],
            [' ','*',' ','*','*',' ',' ',' ','*',' '],
            [' ','*','*','*','*','*','*','*','*',' ']]

def nonogram(inputPic):
    rows = [[0 for x in range(0, len(inputPic[0]))] for x in range(0, len(inputPic[0]))] 
    columns = [[0 for x in range(0, len(inputPic[1]))] for x in range(0, len(inputPic[1]))] 

    groupNumber = 0
    before = 0
    for row in range(0, len(inputPic[0])):
        for column in range(0, len(inputPic[1])):
            if inputPic[row][column] is '*':
                rows[row][groupNumber] += 1
                before = 1
            elif inputPic[row][column] is ' ' and before is 1:
                groupNumber +=1
        groupNumber = 0
    
    groupNumber = 0
    before = 0
    for column in range(0, len(inputPic[1])):
        for row in range(0, len(inputPic[0])):
            if inputPic[row][column] is '*':
                columns[column][groupNumber] += 1
                before = 1
            elif inputPic[row][column] is ' ' and before is 1:
                groupNumber +=1
        groupNumber = 0


    print("Columns:")
    columnsPrint = []
    for column in columns:
        columnsPrint.append(list(filter((0).__ne__, column)))
    print(columnsPrint)

    print("Rows:")
    for row in rows:
        print(list(filter((0).__ne__, row)))

   

nonogram(picture2)
