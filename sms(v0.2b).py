stu = [ ] #empty list
i = 0
def add_data():
    n = input("Enter name")
    a = int(input("Enter age"))
    c = int(input("Enter your present class"))
    student = {
        "name": n,
        "age": a,
        "class": c
    } #Defining a dictionary to store student credentials as a structured unit

    stu.append(student)
def remove_data():
    r = input("Enter the student to be removed")
    for i in range(len(stu)):
        if student["name"] == r:
        
            stu.remove(student) #removes the entire dictionary associated with that student
            print("Removed")

def dis_data():
    for student in stu:
        print("Name:  ",student["name"], "  Age:  ", student["age"], "  Class:  ", student["class"])

print("1.Add student")
print("2.Remove student")
print("3.Display student")
print("4.Exit")

while True:
    d = int(input("Enter decision"))
    if d == 1:
        add_data()
    elif d == 2:
        remove_data()
    elif d == 3:
        dis_data()
    elif d == 4:
        break
    else:
        print("invalid")
