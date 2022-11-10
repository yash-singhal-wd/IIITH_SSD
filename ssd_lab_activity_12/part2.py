from datetime import datetime

# filename = input("Filepath (with extension): ")
f = open("file2.txt")
allLines = f.readlines()
allEntries = list()

f.close()

for eachLine in allLines:
    temp = eachLine.split("\t")
    allEntries.append(temp)

arrLen = len(allEntries)
rowCount = 0
tempCounter = 0
t1 = str()
j_ = 0
i_ = 0

stepCounter_=0
flag = False
for ind in range(arrLen):
    i = allEntries[ind]
    if (i[0] == "\n"):
        tempCounter = 0
        strideCounter = 0
        stepCounter_ = stepCounter_+1
        continue
    else:
        iLen = len(i)
        for j in range(1, iLen):
            if (i[j] != str(0) and i[j] != "\n"):
                newCol = j
                i_ = tempCounter
                j_ = j
                flag = True
                stepCounter_ = stepCounter_-1
                break
        if (flag==True):
            t1 = i[0]
            flag=True
            break
            continue
        tempCounter += 1
    rowCount += 1

for i in allEntries[rowCount:]:
    if (i[0] != "\n"):
        rowCount += 1
    else:
        break

row2 = int("0")
t2 = str()

for eachEntry in allEntries[rowCount:]:
    if (eachEntry[0] == "\n"):
        tempCounter = 0
        
        continue
    else:
        if (eachEntry[j_] != str(0) and tempCounter<i_):
            row2 = tempCounter
            t2 = eachEntry[0]
            break
        tempCounter += 1

strideLen = i_-row2
print("The stride Length is:", round(strideLen,2), "units.")

format = "%H:%M:%S.%f"
t1 = datetime.strptime(t1, format)
t2 = datetime.strptime(t2, format)

numerator = (i_ - row2)
denom =  (t2 - t1).total_seconds()
velocity = numerator / denom
print("Stride velocity is:", round(velocity,2),"units/sec.")

tempvar = (t2 - t1).total_seconds()
tempVar2 = 3/tempvar
steps = tempVar2*60
print("The cadence is:", round(steps,2), "steps/minute.")

