'''
Author    : Aadesh Salecha
Course    : MIT 6.00.1x
Date      : October - November 2015
'''

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name + " says: It is obvious that " + self.name + " says: " + stuff
        
    def lecture(self, stuff):
        return "It is obvious that " + self.name + " says: " + stuff
