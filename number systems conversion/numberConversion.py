def strToList(x:str):
    list = []
    
    for i in range(len(x)):
        list.append(x[i])
    
    return list

def numberToChar(x:int):
    
    if isinstance(x,int):
        match x:
            case 10:
                return 'a'
            case 11:
                return 'b'
            case 12:
                return 'c'
            case 13:
                return 'd'
            case 14:
                return 'e'
            case 15:
                return 'f'

    return x

def charToNumber(x:str):

    if isinstance(x,str):
        match x:
            case "a":
                return 10
            case "b":
                return 11
            case "c":
                return 12
            case "d":
                return 13
            case "e":
                return 14
            case "f":
                return 15
    
    return x
