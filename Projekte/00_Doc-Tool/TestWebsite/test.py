import ast

basicList = ["hallo", "du", "Freak", ["2teDimensionERSTEREintrag", "2teDimensionZWEITEREintrag"]]
print(basicList)
print(type(basicList))
print(len(basicList))
print(basicList[0])
print(basicList[1])
print(basicList[2])
print(basicList[3])
print(basicList[3][0])
print(basicList[3][1])


print("#######")

stringbasicList = str(basicList)
print(stringbasicList)

print(type(stringbasicList))
print(len(stringbasicList))

print("#######")

basiclist = []
basicList2 =  ast.literal_eval(stringbasicList) 
print(basicList2)
print(type(basicList2))
print(len(basicList2))
print(basicList2[0])
print(basicList2[1])
print(basicList2[2])
print(basicList2[3])
print(basicList2[3][0])
print(basicList2[3][1])