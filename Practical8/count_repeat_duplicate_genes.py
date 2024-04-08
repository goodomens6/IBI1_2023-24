import re

xfile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
sac=xfile.read().split(sep='\n')
seq=input("")
output_file=open(seq+"_duplicate_genes.fa","w")

dictionary={}
for line in sac:
    if line.startswith('>'):
        name=line
        dictionary[name]=""
    else:
        dictionary[name]+=line.replace("\n","")

yfile={}
for i in dictionary.keys():
    if "duplication" in i and seq in str(dictionary[i]):
        x=str(dictionary[i]).count(seq)
        name=i.split()[0]+' '+str(x)
        yfile[name]=dictionary[i]

for i in yfile.keys():
    output_file.write(i)
    output_file.write("\n")
    output_file.write(yfile[i])
    output_file.write("\n")
xfile.close()




