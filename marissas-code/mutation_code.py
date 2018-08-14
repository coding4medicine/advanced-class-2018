import random 
f = open("/share/data/ancestry/south-america","r")
str = f.readline() 
length = len(str) 
str = list(str) 
indices = [] 
characters = [] 
nucleotide_options = "ACTG" 
tenp = 0.001*length 
tenp = int(tenp) 

for i in range(0,tenp-1):
    indices.append(random.randint(0,length-1))
    characters.append(random.choice(nucleotide_options)) 
charindex = 0 
for i in indices:
    char = characters[charindex]
    str[i] = char
    charindex = charindex + 1 
finalstr = "".join(str) 
print(finalstr)
