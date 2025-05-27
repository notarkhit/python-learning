groceries = []

def addItem():
    print("Add groceries to the list : (enter x to stop) \n")
    while True:
        item = input("item name: ")
        if item == 'x':
            break

        groceries.append(item)

def showList():
    i=1
    for item in groceries:
        print(f"{i}. {item} ")
        i += 1

while True:
    print("\nGrocery list:")
    print("1. Show list")
    print("2. Add item")
    print("3. Remove item")

    opt = int(input('Enter an option: '))

    if opt == 1:
        showList()

    if opt == 2:
        addItem()
    
