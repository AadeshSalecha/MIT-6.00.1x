'''
Author    : Aadesh Salecha
Course    : MIT 6.00.1x
Date      : October - November 2015
'''
def f(x):
	import math
	return 60*math.e**(math.log(0.5)/55.6 * x)
def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    radiation = 0
    time = int((stop - start) * step)
    #print time
    for i in range(time):
        radiation += f((i*step)+start) * step
    return radiation #* step
    
print radiationExposure(60, 120, 0.5)