#nput.py
import random

possibleLetters = "AGCT"
f = open('asia.txt','r')
message = list(f.read())
randNum = 0
randChar = 0
for i in range(50):
    randNum = random.randint(0,len(message))
    randChar = random.randint(0, 3)
    while message[randNum] == possibleLetters[randChar]:
        randChar = random.randint(0, 3)
    message[randNum] = possibleLetters[randChar]

print("".join(message))

f.close()
