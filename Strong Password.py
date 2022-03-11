numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

def minimumNumber(n, password):
    finalPassword = 0
    if not any(word in numbers for word in password):
        finalPassword += 1
    if not any(word in lower_case for word in password):
        finalPassword += 1
    if not any(word in upper_case for word in password):
        finalPassword += 1
    if not any(word in special_characters for word in password):
        finalPassword += 1
    if len(password) < 6:
        return max(finalPassword, 6 - len(password))
    return finalPassword