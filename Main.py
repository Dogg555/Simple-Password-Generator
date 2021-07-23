#imported modules
import random 
from pathlib import Path





#variables used
password = ''
global passwordFillerAlpha
global passwordFillerSymbols
global passwordFillerNumeric
passwordFillerAlpha = []
passwordFillerNumeric = []
passwordFillerSymbols = []
global lengthOfPassword
lengthOfPassword = 0
alphaNumeric = False
numeric = False
symbols = False
#functions
def alphaNumericCharacterGenerator():
    characters = ["A",'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    joiner = random.choices(characters, k=lengthOfPassword)
    passwordFillerAlpha.append(joiner)

def numericCharacterGenerator():
    characters = ['1','2','3','4','5','6','7','8','9','0']
    joiner = random.choices(characters, k=lengthOfPassword)
    passwordFillerNumeric.append(joiner)


def symbolCharacterGenerator():
    characters = ['!','@','#','$','%','^','&','*','(',')', '~','`','_','-','+','=','{','}','[',']','|',':',';',',','.','<','>','?']
    joiner = random.choices(characters, k=lengthOfPassword)
    passwordFillerSymbols.append(joiner)
    




#main
print("Welcome to this random password generator where you can create any password you want.")
print("This program will start by asking different questions that will help generate your password.")
firstQuestion = int(input("How long do you want your password to be?\n"))
lengthOfPassword = firstQuestion
secondQuestion = input("Do you want aplha numeric characters in your password? (Y for yes and N for no)\n")
secondQuestionUpper = secondQuestion.upper()
if secondQuestionUpper == 'Y':
    alphaNumeric = True
thirdQuestion = input("Do you want numeric characters in your password? (Y for yes and N for no)\n")
thirdQuestionUpper = thirdQuestion.upper()
if thirdQuestionUpper == 'Y':
    numeric = True
fourthQuestion = input("Do you want symbols in your password? (Y for yes and N for no)\n")
fourthQuestionUpper = fourthQuestion.upper()
if fourthQuestionUpper == 'Y':
    symbols = True

if alphaNumeric == True:
    alphaNumericCharacterGenerator()
    passwordFillerAlpha = ''.join(passwordFillerAlpha[0 -1])
    password += passwordFillerAlpha
if numeric == True:
    numericCharacterGenerator()
    passwordFillerNumeric = ''.join(passwordFillerNumeric[0 -1])
    password += passwordFillerNumeric
if symbols == True:
    symbolCharacterGenerator()
    passwordFillerSymbols = ''.join(passwordFillerSymbols[0 -1])
    password += passwordFillerSymbols

password = list(password)


while len(password) != lengthOfPassword:
    random.shuffle(password)
    password.pop()
    if len(password) == lengthOfPassword:
        break

password = ''.join(password)


fileName = input("Type in a name for this file (no extension needed):\n")
    
Path(f'{fileName}.txt').write_text(password)




    








