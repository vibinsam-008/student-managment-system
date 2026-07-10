name = [ ] # Creating a empty list to store names through append
i = 0
def show_menu():
    print("1.Add students")
    print("2.Search student")
    print("3.Remove student")
    print("4.Display student")
def add_students():
    n = input("Enter name")
    name.append(n) #append is used to add the name at the end of the list
    return name #since name is a string it must be returned 

def search_students():
    s = input("Search for a student name")
    for i in range(len(name)): #i must lie in the range of total names enrolled and it is true
        if s == name[i]: #loops till the full initial match with existing ones
            print("Match found", name[i])
            return
        else:
            print("Student not found")
            

def remove_students():
    r = input("Enter the student to be removed")
    for i in range(len(name)):
        if r == name[i]:
            name.remove(r) #removes a student, no matter the position it holds in the list
            print("Removed")
            break

def display_students():
    for i in range(len(name)):
        print("Student Name:", name[i])
menu = show_menu() #shows the menu
while True:
    d = int(input("Enter the decision")) #asks for the tab to be redirected to

    if d == 1: 
        add_students() #calls add student function
    elif d == 2:
        search_students()#calls search student function
    elif d == 3:
        remove_students() # calls remove student function
    elif d == 4:
        display_students() # calls display student function
    else:
        print("Invalid")
