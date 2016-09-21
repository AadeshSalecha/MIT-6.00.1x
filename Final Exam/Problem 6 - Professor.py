'''
Author    : Aadesh Salecha
Course    : MIT 6.00.1x
Date      : October - November 2015
'''

class Professor(Lecturer): 
    def say(self, stuff): 
        return 'Prof. ' +  self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return "Prof. " + self.name + " says: It is obvious that I believe that " + self.name + " says: " + stuff
        
    def lecture(self, stuff):
        return "It is obvious that I believe that " + self.name + " says: " + stuff
