def caesarCipher(text:str, shift:int, toEncrypt:bool):

    ref = "abcdefghijklmnopqrstuvwxyz"

    newText = []

    if toEncrypt:

        for i in range(len(text)):
            ch = text[i]

            if ch == " ":
                newText.append(ch)
            elif ch.capitalize() == ch:
                newText.append( chr((ord(ch) + shift - 65) % 26 + 65) )
            elif ch.capitalize() != ch:
                newText.append( chr((ord(ch) + shift - 97) % 26 + 97) )
            else:
                newText.append(ch)
    
    else:
        for i in text:
            if i.lower() in ref:
                position = ref.find(i.lower())
                newPos = (position - shift) % 26
                newChar = ref[newPos]
                newText.append(newChar)
            else:
                newText.append(i)
    
    
    cipher = ""
    asciiCode = ""

    for i in range(len(newText)):
        cipher += newText[i].capitalize()
        if ord(newText[i].capitalize()) >= 65 and ord(newText[i].capitalize()) <= 97:
            asciiCode += (str(ord(newText[i].capitalize())) + ", ")
        else:
            asciiCode += str(newText[i])

    print(f"{cipher}\n{asciiCode}")


caesarCipher("OLF THSJVST! DHUUH OHUN VBA HMALY ZJOVVS AVKHF?",7 , False)
caesarCipher("NEGROS ORIENTAL STATE UNIVERSITY",20,True)
# caesarCipher("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z", 7, False)

