# CS501: HW4
# Name: Ryan Vas
# Date: 09/17/2018

#Q1
print("Q1")
positive_list = ['good','awesome','excellent','great','efficient','bug-free','user-friendly']
negative_list = ['bad','bugs','boring','tiresome','poor performance','inefficient']
puncList = ['.',',','!','?']

pCount = 0
nCount = 0

inp = ''
intext = ''
intextList = []

pos = {}
neg ={}

while (inp !='\end'):
    inp = input()
    instr = ''
    
    for i in inp:
        if i not in puncList:
            instr = instr + i
         
    intextList.append(instr)
    
    if '\end' in inp: break

intext = ' '.join(intextList).split('\end')[0]
intextUc = intext.lower()
intextSplit = intextUc.split()

if intext.strip == '':
    output = 'Indeterminate'
else:
    for param in positive_list:
        pos[param] = 0
        for word in intextSplit:
            if param == word.strip():
                pCount = pCount + 1
                pos[param] = pos[param] + 1

    for param in negative_list:
        neg[param] = 0
        for i,word in enumerate(intextSplit):
         
            if param == word.strip():
                nCount = nCount + 1
                neg[param] = neg[param] + 1

            if param == 'poor performance' and i != len(intextSplit)-1:
                if word == 'poor' and intextSplit[i+1] == 'performance':
                    nCount = nCount + 1
                    neg[param] = neg[param] + 1
    
    if pCount == 0 and nCount == 0:
        output = 'Indeterminate'
    elif pCount > nCount:
        output = 'Positive'
    elif nCount > pCount:
        output = 'Negative'
    else:
        output = 'Indeterminate'

print(output)        
#new comment
#Q2
print("Q2")  
primeList = []     
num1 = int(input())
num2 = int(input())

for aNumber in range(2,num1+1):
    isPrime = True
    for i in range(2,aNumber):
        if (aNumber%i == 0):
            isPrime = False
    if isPrime: primeList.append(aNumber)  
    
closestNumber = min(primeList, key = lambda j: abs(num2 - j))  
print ('Closest prime number: {}'.format(closestNumber))
      
            
  









