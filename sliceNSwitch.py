def sliceNSwitch(elements, blockSize):
    for x in range(0, len(elements), blockSize):
        print(elements[x:(x+blockSize)][::-1])
    

sliceNSwitch([1,5,7,9,11,13,15,17], 3)
