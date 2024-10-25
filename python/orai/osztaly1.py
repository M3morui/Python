import datetime as dt

class Member:
    def __init__(self, lastname, firstname):
        self._lastname = lastname
        self._firstname = firstname
        self.__date_joined = dt.date.today()
        self.__is_active = True

    def join_date(self):
        return f"{self.__date_joined} csatlakozott a munkacsoporthoz."
    
    def member_since(self):
        return "Igen" if self.__is_active else "Nem"
    
    @property
    def is_active(self):
        return self.__is_active
    
    @is_active.setter
    def is_active(self, value):
        self.__is_active = value

new_member = Member("Rocco", "Moe")
print(f"Vezetéknév: {new_member._lastname}")
print(f"Keresztnév: {new_member._firstname}")
print(new_member.join_date())
print(f"isActive válzozó lekérése @property-vel: {new_member.is_active}")
new_member.is_active = False
print(f"Aktív tag-e: {new_member.member_since()}")


print("-"*30)


new_member2 = Member("John", "Doe")
# new_member._firstname = "John"
# new_member._lastname = "Doe"
print(f"Vezetéknév: {new_member2._lastname}")
print(f"Keresztnév: {new_member2._firstname}")
print(new_member2.join_date())
print(f"isActive válzozó lekérése @property-vel: {new_member2.is_active}")
new_member2.is_active = False
print(f"Aktív tag-e: {new_member2.member_since()}")