class Person:
    def  __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.firstName == other.firstName and self.lastName == other.lastName 
    
    def __str__(self):
        return "First Name = " + self.firstName + ", Last Name = " + self.lastName

class SpecialAgent(Person):
    def __init__(self, firstName, lastName, secretName):
        super().__init__(firstName, lastName)
        self.secretName = secretName
    
    def __str__(self):
        return Person.__str__(self) + ", Secret Name = " + self.secretName


if __name__ == "__main__":
    specialAgent = SpecialAgent("John", "Smith", "Viper")
    print(specialAgent)
