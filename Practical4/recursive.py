#function: Calculate and display the first five answers of a recursive sequence
i=1
j=4 #the first answer is 4
print(j)
while i<=4: #the loop runs 4 times so we have 5 answers
    j=2*j+3 #the sequence
    print(j) #output the answer
    i+=1