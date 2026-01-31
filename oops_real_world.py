# Real world example : User System
class User:
  def __init__(self,username,email):
    self.username = username
    self.email = email
  def display(self):
    return f"Username:{self.username},Email{self.email}"

class Admin(User):
  def __init__(self,username,email,role):
    super().__init__(username,email)
    self.role = role
  def display(self):
    return f"{super().display()},Role:{self.role}"

admin1 = Admin("muskan","muskan@gmail.com","Admin")
print(admin1.display)    
  
