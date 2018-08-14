find = open("/share/data/ancestry/find.txt","r")
findline = find.readline()

asia = open("/share/data/ancestry/asia","r")
asialine = asia.readline()

africa = open("/share/data/ancestry/africa","r")
africaline = africa.readline()

southamerica = open("/share/data/ancestry/south-america","r")
saline = southamerica.readline()

europe = open("/share/data/ancestry/europe","r")
europeline = europe.readline()


asiacount = 0
africacount = 0
sacount = 0
europecount = 0

for i in range(0,len(findline)-1):
	findcomp = findline[i]
	
	if asialine[i] == findcomp:
		asiacount = asiacount + 1
	if africaline[i] == findcomp:
		africacount = africacount + 1
	if saline[i] == findcomp:
		sacount = sacount + 1
	if europeline[i] == findcomp:
		europecount = europecount + 1

print("Asia matches: " + str(asiacount))
print("Africa matches: " + str(africacount))
print("South America matches: " + str(sacount))
print("Europe matches: " + str(europecount))


if asiacount > africacount and asiacount > europecount and asiacount > sacount:
	print("The sample is from Asia")
if africacount > asiacount and africacount > europecount and africacount > sacount:
	print("The sample is from Africa")
if sacount > asiacount and sacount > europecount and sacount > africacount:
	print("The sample is from South America")
if europecount > sacount and europecount > africacount and europecount > asiacount:
	print("The sample is from Europe")

