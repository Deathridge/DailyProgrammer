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

        if current == goal:
            pathTaken = []
            while current.parent:
                pathTaken.append(current)
                current = current.parent
            pathTaken.append(current)
            return path[::-1]
        
        successorList = successors(current,nodes)
        for successor in successorList:
            successor.g = current.g + current.move_cost(successor)
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
