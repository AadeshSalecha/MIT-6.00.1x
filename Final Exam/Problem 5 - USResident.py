'''
Author    : Aadesh Salecha
Course    : MIT 6.00.1x
Date      : October - November 2015
'''
class USResident(Person):
    def __init__(self, name, status):
        Person.__init__(self, name)
        if status not in ["citizen", "legal_resident", "illegal_resident"]:
            raise ValueError
        self.status = status
        
    def getStatus(self):
         return self.status