class Person:
    def __init__(self, first_name, email, age):
        self.first_name = first_name
        self.email = email # Call email() method to set email
        self.age = age

    # Public methods
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        self.__email = new_email

    @property
    def age(self):
        return self._get_age()

    @age.setter
    def age(self, age):
         self._set_age(age)

    # Private method
    def _get_age(self):
        return self.__age

    def _set_age(self, age):
        self.__age = age

jesus = Person('Jesus', 'jesu@mail.com', 21)
print(jesus.email)
jesus.email = 'lla@mail.com'
print(jesus.email)
print(jesus.age)
jesus.age = 22
print(jesus.age)

class Worker(Person):
    def __init__(self, first_name, email, age, company):
        Person.__init__(self, first_name, email, age)
        self.company = company

    def get_company(self):
        return self.company

a = Worker('Adam', 'adam@email.com', 32, 'Awezon')
print(a.age)
print(a.get_company())