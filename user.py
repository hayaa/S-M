class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def print_user(self):
        print(f'User: {self.full_name()}, Email: {self.email}')

# Testing the class
user = User('John', 'Doe', 'john.doe@mail.com')
user.print_user()  # Prints "User: John Doe, Email: john.doe@mail.com"
