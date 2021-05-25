class Passenger():
    def __init__(self, firstName = None, lastName = None, age = None): 
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getFullName(self):
        return "%s %s"%(self.getFirstName(), self.getLastName())

    def getAge(self):
        return self.age

    def isChild(self):
        if self.getAge() < 13:
            return True
        else:
            return False

    def isSenior(self):
        if self.getAge() > 60:
            return True
        else:
            return False
        







