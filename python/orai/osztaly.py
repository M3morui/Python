import datetime as dt
class Member:
    """Create a new member."""

    # osztálynaka konstruktora
    def __init__(self, uname, fname):
        #osztály attributumai
        self.username = uname
        self.fullname = fname
        self.date_join = dt.date.today()
        self.is_active = True

    def show_datejoined(self):
        return f"{self.fullname} joined on {self.date_join}"
    
    def __str__(self):
        return f"{self.username} -> {self.fullname}"

new_guy = Member("Rambo", "Rocco Moe")
new_guy2 = Member("John", "John Doe")
# print(new_guy)
# print(new_guy.username)
# print(new_guy.fullname)
# print(type(new_guy))
# new_guy.username = "Princess"
# print(new_guy.username)
# print(new_guy.fullname)
# print(new_guy.date_join)
# print(new_guy.show_datejoined())
# print("Active: ",new_guy.is_active)
guys_list = [Member("Rambo", "Rocco Moe"), Member("John", "John Doe"), Member("Jane", "Jane Doe")]
for guy in guys_list:
    print(guy)