import AStar
from AStar import Node, gridtoNodes, AStar

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
    
    originx = movingNode.x
    originy = movingNode.y

    movingNode.x = swappingNode.x
    movingNode.y = swappingNode.y
    swappingNode.x = originx
    swappingNode.y = originy

    movingNodeChildren = childGrid[movingNode.value]
    childGrid[movingNode.value] = childGrid[swappingNode.value]
    childGrid[swappingNode.value] = movingNodeChildren

    for node in childGrid[movingNode.value]:
        if node.value is movingNode.value:
            node.value = swappingNode.value
    for node in childGrid[swappingNode.value]:
        if node.value is swappingNode.value:
            node.value = movingNode.value

    
    
    return [childGrid, grid]

grid = [[4,6,2,14],[15,8,13,1],[10,5,9,12],[7,11,16,3]]

goalGrid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
newgrid = gridtoNodes(grid)


def getGoal(movingNode, grid, goalGrid):
    for r in range(0, len(grid)):
        for c in range(0, len(grid)):
            if movingNode.value is goalGrid[r][c]:
                goal = Node(c+1,r+1, grid[r][c])
                
    return goal

def getNextmove(movingNode, nodeGrid):
    goalNode = getGoal(movingNode,grid,goalGrid)
    nextSpot = AStar(movingNode, goalNode, newgrid)
    
    
    if len(nextSpot) > 1:
        return nextSpot[1]
    else:
        return nextSpot[0]



def getLocation(value, grid):
    for row in range(0, len(grid)):
        for column in range(0, len(grid[row])):
            if grid[row][column] is value:
                return Node(column+1, row+1, value)

def test(grid, goalGrid, newgrid):
    while grid is not goalGrid:
        for row in range(0, len(grid)):
            for column in range(0, len(grid[row])):
            
                nodeValue = grid[row][column]
        
                node = Node(row+1,column+1,nodeValue)
                goal = getGoal(Node(column+1, row+1, nodeValue), grid, goalGrid)                        
                   
                nextSpot = getNextmove(node, newgrid)
                
                [newgrid, grid] = move(node, nextSpot, newgrid, grid)            
                
                
            
