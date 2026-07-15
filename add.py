from data import dat
def add():
    n = input("Enter your name")
    dob = input("Enter Date of Birth")
    schl = input("Enter School")
    c = float(input("Enter your 12th average"))

    data = {
        "name":n,
        "DOB":dob
        "school":schl,
        "avg":c
    }
dat.append(data)
