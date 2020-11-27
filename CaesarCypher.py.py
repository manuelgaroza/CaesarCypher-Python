def getDoubleAlphabet(alphabet):                      
   doubleAlphabet = alphabet + alphabet
   return doubleAlphabet


def getMessage():                                        #function to return the message you want to encrypt
    message=input("Please enter the message you want to encrypt: ")
    return message   


def getCipherKey():                             #function to return the cypher key
   shiftAmount = input( "Please enter a key (whole number from 1-25): ") 
   return shiftAmount

                          
def encryptMessage(message, cipherKey, alphabet):   #function to encrypt
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

def decryptMessage(message, cipherKey, alphabet):      #function to decrypt
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

def runCaesarCipherProgram():                            #function to run all the script
    myAlphanumeric="ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    print(f"Alphanumeric: {myAlphanumeric}" )
    myAlphanumeric2 = getDoubleAlphabet(myAlphanumeric)
    print(f"Alphanumeric2:{myAlphanumeric2}")
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphanumeric2)
    print(f"Encrypted Message: {myEncryptedMessage}")
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey,myAlphanumeric2)
    print(f"Decypted Message: {myDecryptedMessage}")
    
runCaesarCipherProgram()    
