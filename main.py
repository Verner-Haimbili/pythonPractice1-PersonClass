class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def __str__(self):
        return f"Person [name={self.name}, age={self.age}]"


class AppClass:
    @staticmethod
    def main():
        p1 = Person("David", 22)
        print(p1)


# Run the main method below
AppClass.main()
