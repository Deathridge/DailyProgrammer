import math, random, string

def hammingDistance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Strings not equal length")
    return sum(bool(ord(ch1) - ord(ch2)) for ch1, ch2 in zip(s1,s2))

def fitnessFunction(text,goal):
    hdist = hammingDistance(text,goal)
    fitness = hdist
    #for l in range(0, len(text)):
    #   fitness = fitness + abs(ord(text[l]) - ord(goal[l]))/10
    return fitness
    
def begin():
   
    goal = 'The end of the world as we know it!'
    rate = 1/len(goal)
    text = ''.join(random.choice(string.printable) for i in range(len(goal)))
    generation = 1 
    while fitnessFunction(text,goal) > 0:
        previous = text
        text = evolve(text, previous, goal, rate )
        generation += 1
        print(text, generation)
    
    
def mutate(text,previous, rate):
    textLength = len(text)
    textList = list(text)
    previousList = list(previous)
    childList = textList
    for l in range(0, textLength):
        if l < int(textLength/2):
            childList[l] = previousList[l]
        else:
            childList[l] = textList[l]
        
    for letter in range(0, textLength):
        if random.randrange(0,10) < rate*10:
            textList[letter] = random.choice(string.printable)

    return "".join(textList)

def evolve(text, previous, goal, rate):
    #evolutionDictionary = {text: fitnessFunction(text,goal)}
    evolutionDictionary = {}
    for m in range(0, 100):
        mutatedString = mutate(text,previous, rate)
        fitnessValue = fitnessFunction(mutatedString, goal)
        evolutionDictionary[mutatedString] = fitnessValue
    minString = min(evolutionDictionary, key=lambda x: evolutionDictionary.get(x))
    
    return minString
    

begin()
