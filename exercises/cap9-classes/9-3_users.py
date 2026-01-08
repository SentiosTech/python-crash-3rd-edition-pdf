class User:
    def __init__(self, first_name, last_name, **user_info): #al usar kwargs se usa el for y metodo items() en forma de diccionario para multiples parametros
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info

    def describe_user(self):
        print("user description:")
        print(f'first name: {self.first_name}')
        print(f'last name: {self.last_name}')
        print(f'user_info:')
        for key, value in self.user_info.items():
            print(f'{key}: {value}')

    def greet_user(self):
        print("greeting user:")
        print(f'Hello, {self.first_name} {self.last_name}')
        print("here is your profile information")
        for key, value in self.user_info.items():
            print(f'{key}: {value}')

user1 = User("Alice", "Smith", age=25, mail="alice@example.com", country="Spain")
user1.describe_user()
print("-"*10)
user1.greet_user()
print("-"*50)
user2 = User('hotroad', 'hudson', age=21, mail='hothudson@gmail.com',country='france') #*kwargs se describe es que y el valor
user2.describe_user()
print("-"*10)
user2.greet_user()
