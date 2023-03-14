class Account():
    def __init__(self, username, password, email, phone_number):
        self._username = username
        self._password = password
        self._email = email
        self._phone_number = phone_number

class User(Account):
    def __init__(self, username, password, email, phone_number, full_name):  
        super().__init__(username, password, email, phone_number)
        self.__full_name = full_name

class Admin(Account):
    def __init__(self, username, password, email, phone_number, name):  
        super().__init__(username, password, email, phone_number)
        self.__name = name

user = User('GAGa_boo', 'password123','test@gmail.com','0903031788','Natdanai')

def login(username, password):
    
    if username == user._username and password == user._password:
        return 'User login successful!'
    else:
        return 'Login failed.'
#print(user.__full_name)  
