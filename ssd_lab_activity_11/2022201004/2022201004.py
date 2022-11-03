import csv

filename = "lab_11_data.csv"

with open(filename) as temp:
    reader = csv.reader(temp)
    allLines = list(reader)

#helper function
# listRemover = lambda allList, index : allList.pop(index)

convertToFloat1= lambda list_: float(list_[1])
convertToFloat2= lambda list_: float(list_[2])
convertToFloat3= lambda list_: float(list_[3])

#Solution Part1
output1 = open('output1', 'w')
for eachList in allLines:
    row = eachList[0: len(eachList)-6]
    string=""
    for eachEle in row:
        string = string + eachEle + " "
    string = string + "\n"
    output1.write(string)
    
output1.close()

#Solution Part2`
allLines = []
filename = "output1"
with open(filename) as temp:
    reader = temp.readlines()
    # print(reader)
    for i in reader:
        tempList = i.split()
        tempList[1] = tempList[1].replace(",", "")
        tempList[2] = tempList[2].replace(",", "")
        tempList[3] = tempList[3].replace(",", "")
        allLines.append(tempList)
    
del allLines[0]
updatedList = list(filter(lambda x: False if float(x[-1])<-3 else True, allLines))

for i in updatedList:
    i[1] = i[1].replace(",", "")
    i[2] = i[2].replace(",", "")
    i[3] = i[3].replace(",", "")

#Solution Part 3
openList = list(map(convertToFloat1, updatedList))
highList = list(map(convertToFloat2, updatedList))
lowList = list(map(convertToFloat3, updatedList))

# output1
print(sum(openList)/len(openList))
print(sum(highList)/len(highList))
print(sum(lowList)/len(lowList))

output2 = open("avg_output.txt", "w")
output2.write(str(sum(openList)/len(openList)) + "\n")
output2.write(str(sum(highList)/len(highList)) + "\n")
output2.write(str(sum(lowList)/len(lowList)) + "\n")

#Solution part 4 and 5
with open("stock_output.txt", "w") as mainFile:
    charEntered = input("Enter uppercase alphabet: ")
    for item in updatedList:
        if(item[0][0]==charEntered):
            mainFile.write(str(item)+'\n')
            print("Written successfully")