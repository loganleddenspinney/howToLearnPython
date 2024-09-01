itemList = [1,2,3,4,5,2, 3, 67, 1]

x = 0
for item in itemList:
    if item > x:
        x = item

print(x)

print(max(itemList))