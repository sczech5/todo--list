#To-Do List
#Morgan and Steph

#Initialize 

shoppingList = []


#Functions

#asks user for item to add to list
#adds item and prints list
def addTask():
    additems = input("Which items would you like to add to your shopping list?:")
    shoppingList.append(additems)
    print(shoppingList)

#prints the user's shopping list
def viewList():
    print(shoppingList)

#asks user for item to mark as completed
#finds index and places check next to item
def markDone():
    completedtask = input("Which item would you like to mark as completed?: ")
    i = shoppingList.index(completedtask)
    shoppingList[i] = completedtask + " X"
    print(shoppingList)

#asks user for item to remove from list
#removes item and prints list
def removeTask():
    takeitems = input("Which items would you like to remove from your shopping list?:")
    shoppingList.remove(takeitems)
    print(shoppingList)

def removeAll():
    shoppingList.clear()
    print(shoppingList)

def sortLetter():
    list = sorted(shoppingList)
    print(list)

def countItems():
    print(len(shoppingList))





#Main

while True:
    print("Welcome to your To-Do list. Please choose which operation you would like to perform.")
    print("1. Add a task to the to-do list \n 2. View the current to-do list \n 3. Mark a task as completed \n 4. Remove a task from the to-do list \n 5. Remove all tasks from the to-do list \n 6. Sort the list alphabetically \n 7. Count the # of Items on the To-do List \n 8. Exit the program")
    option = int(input("Which option would you like to choose: "))

 
    if option == 1:
        addTask()
    if option == 2:
        viewList()
    if option == 3:
        markDone()
    if option == 4:
        removeTask()
    if option == 5:
        removeAll()
    if option == 6:
        sortLetter()
    if option == 7:
        countItems()
    if option == 8:
        print("Thank you for using To-Do List. Goodbye.")
        break