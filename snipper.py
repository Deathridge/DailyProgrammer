def snipper(originalString, toRemove):
    output = originalString
    for item in toRemove:        
        output = str(output).replace(str(item), "")

    return output

snipper("testing string", "ei ")
