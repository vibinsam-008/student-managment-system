name = [ ]
i = 0
def show_menu():
    print("1.Add students")
    print("2.Search student")
    print("3.Remove student")
    print("4.Display student")
def add_students():
    n = input("Enter name")
    name.append(n)
    return name

def search_students():
    s = input("Search for a student name")
    for i in range(len(name)):
        if s == name[i]:
            print("Match found", name[i])
            return
        else:
            print("Student not found")
            

def remove_students():
    r = input("Enter the student to be removed")
    for i in range(len(name)):
        if r == name[i]:
            name.remove(r)
            print("Removed")
            break

def display_students():
    for i in range(len(name)):
        print("Student Name:", name[i])

while True:

    menu = show_menu()

    d = int(input("Enter the decision"))

    if d == 1:
        add = add_students()
    elif d == 2:
        search = search_students()
    elif d == 3:
        remove = remove_students()
    elif d == 4:
        display = display_students()
    else:
        print("Invalid")
