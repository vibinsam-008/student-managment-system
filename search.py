from data import dat
def search():
  s = input("Enter date of birth or name of the student)
  if data["name"] == s or data["DOB"] == s:
    for name in dat:
      print("Name: ", data["name"])
      print("DOB:  ", data["DOB"])
      print("School:  ", data["school"])
      print("Average in class 12:  ", data["avg"])
    
