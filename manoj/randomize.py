##########################
# Changing sequence at
# random locations
##########################

import random

file=open("/share/data/ancestry/africa","r")
seq=file.readline()
seqlist=list(seq)


# We are making 10 random changes

for i in range(10):
	pos=random.randint(0,len(seqlist))
	if seqlist[pos]=='A': changes=['C','G','T']
	if seqlist[pos]=='T': changes=['C','G','A']
	if seqlist[pos]=='G': changes=['C','A','T']
	if seqlist[pos]=='C': changes=['A','G','T']

	nucl=changes[random.randint(0,2)]
	seqlist[pos]=nucl

seq="".join(seqlist)
print seq
