import math, random, string

#Calculate hamming distance between two strings as a fitness function
def hammingDistance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Strings not equal length")
    return sum(bool(ord(ch1) - ord(ch2)) for ch1, ch2 in zip(s1,s2))

#Base mutation rate on length of the goal string, loop evolution while the goal isnt reached.    
def begin():
   
    goal = 'The end of the world as we know it!'
    rate = 1/len(goal)
    text = ''.join(random.choice(string.printable) for i in range(len(goal)))
    generation = 1 
    while hammingDistance(text,goal) > 0:
        previous = text
        text = evolve(text, previous, goal, rate )
        generation += 1
        print(text, generation)

#Use previous and current string to create a 50/50 split child and then mutate
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

#Generate 100 mutations and compare for fitness, return the fittest.
def evolve(text, previous, goal, rate):
    #evolutionDictionary = {text: hammingDistance(text,goal)}
    evolutionDictionary = {}
    for m in range(0, 100):
        mutatedString = mutate(text,previous, rate)
        fitnessValue = hammingDistance(mutatedString, goal)
        evolutionDictionary[mutatedString] = fitnessValue
    minString = min(evolutionDictionary, key=lambda x: evolutionDictionary.get(x))
    
    return minString
    

begin()
