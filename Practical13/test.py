BLOSUM62_DATA=open('BLOSUM62.txt','rt')
matrix=BLOSUM62_DATA.read().split("\n")
matrix1=[]
for i in matrix:
    i=i.split()
    matrix1.append(i)
BLOSUM62={}

for i in matrix1[0]:
    BLOSUM62[i]={}
for i in range(1,len(matrix1)):
    key=matrix1[i][0]
    for j in range(1,len(matrix1[i])):
        BLOSUM62[matrix1[0][j-1]][key]=matrix[i][j]

print(BLOSUM62)