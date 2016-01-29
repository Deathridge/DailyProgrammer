import aStar
from aStar import Node, gridToNodes, aStar

def move(movingNode, swappingNode, childGrid, grid):
    movingNodeOriginal = movingNode.value
    originalmovingNode = []
    for row in range(0, len(grid)):
        for column in range(0, len(grid[row])):
            if grid[row][column] is movingNode.value:
                
                grid[row][column] = swappingNode.value
                originalmovingNode = [row,column]               
                
            else:
                if grid[row][column] is swappingNode.value:
                    if [row,column] is not originalmovingNode:
                        grid[row][column] = movingNodeOriginal
    print(grid)
    childGrid = gridToNodes(grid)
    
    
    return [childGrid, grid]

grid = [[4,6,2,14],[15,8,13,1],[10,5,9,12],[7,11,16,3]]
grid2 = [[1, 2, 3, 4], [15, 6, 14, 8], [9, 10, 13, 12], [7, 11, 5, 16]]
goalGrid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
newgrid = gridToNodes(grid)


def getGoal(movingNode, grid, goalGrid):
    for r in range(0, len(grid)):
        for c in range(0, len(grid)):
            if movingNode.value is goalGrid[r][c]:
                goal = Node(c+1,r+1, grid[r][c])
                
    return goal

def getNextmove(movingNode, nodeGrid):
    goalNode = getGoal(movingNode,grid,goalGrid)
    nextSpot = aStar(movingNode, goalNode, newgrid)

    return nextSpot



def getLocation(value, grid):
    for row in range(0, len(grid)):
        for column in range(0, len(grid[row])):
            if grid[row][column] is value:
                return Node(column+1, row+1, value)

def test(grid, goalGrid, newgrid):
    while grid is not goalGrid:
        for row in range(0, len(grid)):
            for column in range(0, len(grid[row])):
            
                nodeValue = (row+1)*(column+1)
                
                node = getLocation(nodeValue,grid)
                goal = getGoal(node, grid, goalGrid)                        

                if [node.x,node.y] != [goal.x,goal.y]:
                    nextSpot = getNextmove(node, newgrid)
                    
                    for spot in nextSpot:
                        print(nodeValue,spot.value)
                        [newgrid, grid] = move(node, spot, newgrid, grid)                      
            
            
               
                    
                
                
            
