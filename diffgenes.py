FILE = open("cath.expression.Johnston.p01.txt")

Diffgenes = []

for line in FILE: 
	Diffgenes.append(line.split()[0].lstrip('"').strip('"'))
FILE.close()
FILE = open("transcripts.txt")
OUT = open("DEfasta_Johnstonp1.fa", 'a')
gate = 0 
for line in FILE: 
		if line[0] == '>': 
			try:
				if line.split()[1].strip().lstrip('gene=') in Diffgenes:
					OUT.write(line)
					gate=1
				else: 
					gate=0
			except(IndexError):
				print line 
		else: 
			if gate==1:
				OUT.write(line)
FILE.close()
OUT.close()	