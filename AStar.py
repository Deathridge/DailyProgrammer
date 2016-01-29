import math

class Node:
    """ Node in search """
    def __init__(self, x,y,value):
        self.parent = None
        self.x = x
        self.y = y
        self.g = 0
        self.h = 0
        self.value = value
    def cost(self, other):
        return 0 if self.value == '.' else 1

def successors(currentNode, nodes):
    """ Assumes that the nodes will be a dictionary containing a list of successor nodes"""
    
    successors = nodes[currentNode.value]
    return successors
    
def manhattan(current, successor):
    x1 = current.x
    x2 = successor.x
    y1 = current.y
    y2 = successor.y
    return (abs(x1-x2) + abs(y1-y2))

def gridToNodes(grid):
    nodeChildren = {}
    for row in range(0, len(grid)):
        for column in range(0,len(grid[0])):
            nodeChildren[grid[row][column]] = []
            if row-1 >= 0:
                rm1 = Node(column +1,row-1 +1,  grid[row-1][column])
                nodeChildren[grid[row][column]].append(rm1)
            if column-1 >= 0:
                cm1 = Node(column-1 +1,row+1,  grid[row][column-1])
                nodeChildren[grid[row][column]].append(cm1)
            if row + 1 < len(grid):
                rp1 = Node(column+1,row+1 +1,  grid[row+1][column])
                nodeChildren[grid[row][column]].append(rp1)
            if column + 1 < len(grid[0]):
                cp1 = Node(column+1 +1,row +1,  grid[row][column+1])
                nodeChildren[grid[row][column]].append(cp1)            
             
    return nodeChildren
            

    
def aStar(start, goal, nodes):
    openList = set()
    closed = set()

    openList.add(start)    
    while openList:
        current = min(openList, key=lambda o: o.g + o.h)

        if current.value == goal.value:
            pathTaken = []
            while current.parent:
                
                pathTaken.append(current)
                current = current.parent
           
            pathTaken.append(current)
            
            return pathTaken[::-1]
        
        successorList = successors(current,nodes)
        
        for successor in successorList:
            if successor in closed:
                continue
            tentativeg = current.g + current.cost(successor)
            if successor not in openList:
                openList.add(successor)

            elif tentativeg >= successor.g:
                continue
            
            successor.g = tentativeg
            successor.h = manhattan(goal, successor)          
            successor.parent = current
            
        openList.remove(current)
        closed.add(current)
    raise ValueError('No path was found')

sA = [Node(1,2,'B'), Node(2,1,'D')]
sB = [Node(1,1,'A'), Node(2,2,'E'), Node(1,3,'C')]
sC = [Node(1,2,'B'), Node(2,3,'F')]
sD = [Node(1,1,'A'),Node(2,2,'E')]
sE = [Node(3,2,'H'),Node(2,3,'F')]
sF = [Node(2,2,'E'),Node(3,3,'I')]
sG = [Node(2,1,'D'),Node(3,2,'H')]
sH = [Node(3,1,'G')]
sI = [Node(3,2,'H')]

nodes = {'A':sA, 'B':sB, 'C':sC,'D':sD,'E':sE,'F':sF, 'G':sG, 'H':sH, 'I':sI}





