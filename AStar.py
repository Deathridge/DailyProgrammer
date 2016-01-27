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
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def AStar(start, goal, nodes):
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
            successor.g = current.g + current.cost(successor)
            successor.h = manhattan(goal, successor)
            successor.parent = current
            addSuccessor = True
            
            for node in openList:
                if node.x is successor.x and node.y is successor.y:
                    if (node.g + node.h) < (successor.g + successor.h):
                        addSuccessor = False
            for node in closed:
                if node.x is successor.x and node.y is successor.y:
                    if (node.g + node.h) < (successor.g + successor.h):
                        addSuccessor = False
            if addSuccessor:
                openList.add(successor)
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
