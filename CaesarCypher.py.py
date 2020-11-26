def getDoubleAlphabet(alphabet):
   doubleAlphabet = alphabet + alphabet
   return doubleAlphabet


def getMessage():
    message=input("Please enter the message you want to encrypt: ")
    return message   


def getCipherKey():
   shiftAmount = input( "Please enter a key (whole number from 1-25): ")
   return shiftAmount

                          
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        
        newPosition = position + int(cipherKey)
        
        if currentCharacter in alphabet:
            encryptedMessage  += alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage  

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

def runCaesarCipherProgram():
    myAlphanumeric="ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    print(f"Alphanumeric: {myAlphanumeric}" )
    myAlphanumeric2 = getDoubleAlphabet(myAlphanumeric)
    print("Alphanumeric2: "+ myAlphanumeric2)
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphanumeric2)
    print("Encrypted Message: " + myEncryptedMessage)
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey,myAlphanumeric2)
    print('Decypted Message: '+myDecryptedMessage)
    
runCaesarCipherProgram()    
