list = [1, 2, 3, 4, "string-1", "string-2"]

el = list[5]

print("Minha lista:", list)
print("Elemento 5: ", el)

# Fatiamento (Slicing)
print("Lista 0:4", list[:4])
print("Lista 4:5", list[4:])
print("Lista 2:4", list[2:4])

def getList(interval, myList): 
  print('Interval is:', myList[interval[0]:interval[1]])

getList([2, 6], list)