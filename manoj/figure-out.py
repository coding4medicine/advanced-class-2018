##########################################
#	check ancestry of given sequence
##########################################

f=open("asia","r")
asia=f.readline()
f.close()

f=open("africa","r")
africa=f.readline()
f.close()

f=open("south-america","r")
south=f.readline()
f.close()

f=open("europe","r")
europe=f.readline()
f.close()

f=open("find.txt","r")
given=f.readline()
f.close()

# four count vecto
ca=0
cf=0
cs=0
ce=0
for i in range(len(given)):
	if(given[i]!=asia[i]): ca+=1
	if(given[i]!=africa[i]): cf+=1
	if(given[i]!=south[i]): cs+=1
	if(given[i]!=europe[i]): ce+=1

print "asia=",ca
print "africa=",cf
print "south america=",cs
print "europe=",ce

