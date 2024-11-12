class Student:
    def __init__(self, username, fullname):
        self.username = username
        self.fullname = fullname

    
tanulo1 = Student("redavid", Rédai Dávid")
tanulo2 = Student("bri", "Sinka Brigitta")

                 
print(f"Tanuló neve: {tanulo1.fullname}")
print(f"Nickneve: {tanulo1.username}")



