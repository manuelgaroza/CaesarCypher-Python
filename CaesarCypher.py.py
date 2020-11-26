def getDoubleAlphabet(alphabet):
   doubleAlphabet = alphabet + alphabet
   return doubleAlphabet


def getMessage():
    message=str(input("Please enter a message: "))
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
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    print(f"Alphabet: {myAlphabet}" )
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print("Alphabet2: "+ myAlphabet2)
    myMessage = input("Write a message: ")
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print("Encrypted Message: " + myEncryptedMessage)
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey,myAlphabet2)
    print('Decypted Message: '+myDecryptedMessage)
    
runCaesarCipherProgram()    