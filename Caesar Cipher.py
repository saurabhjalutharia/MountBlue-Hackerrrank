import sys
import string

def caesarCipher(inputString, key):
	lowerCase = string.ascii_lowercase
	upperCase = string.ascii_uppercase
    cipherString = []
    for c in inputString:
        if c.isupper():
            cipherString.append(upperCase[(upperCase.index(c)+key)%len(upperCase)])			#len(upperCase) OR 26
        elif c.islower():
            cipherString.append(lowerCase[(lowerCase.index(c)+key)%len(lowerCase)])
        else:
            cipherString.append(c)
    res = "".join(map(str, cipherString))          
    return res
    

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)