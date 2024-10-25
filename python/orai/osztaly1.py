class Member:
    def __init__(self, lastname, firstname):
        self._lastname = lastname
        self._firstname = firstname

new_member = Member("Rocco", "Moe")
print(new_member._lastname)
print(new_member._firstname)