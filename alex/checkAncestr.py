a = open('asia.txt','r')    #The first reference point

b = open('europe.txt', 'r')  #The second reference point

c = open('africa.txt', 'r')  #The third reference point

d = open('america.txt', 'r') #The fourth reference point

references = (a.read(), b.read(), c.read(), d.read())

e = open('unknown.txt', 'r') #The genome we are trying to determine
check = e.read()

#For the purposes of this program, we will assume all strings are of identical length

refDiff = (0, 0, 0, 0) #These 4 integers will record the number of differences between unknown and the four reference points

for i in range(len(check)):
    for j in range(len(refDiff)):
        if e[i] != references[j][i]:
            refDiff[j] = refDiff[j] + 1
