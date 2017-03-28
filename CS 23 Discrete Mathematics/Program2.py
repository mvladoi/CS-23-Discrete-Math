import timeit
import math 

 


def isclose(a, b):
    return abs(b - a) <= 0.00005



def estimate_big_o(fun):
    s = []
    i = 2**6
    while (i <= 2**12): 
     seconds = 0;
     seconds += timeit.timeit(
     stmt   = '%s(%d)' % (fun.__name__, i),            # formatted string: fun(10)
     setup  = 'from __main__ import %s' % fun.__name__, # make sure fun is visible
     number = 4                                        # number of calls
     )

     if(i< 2**14):
        i*=i
     else:
        i = (2**14) +1
        
     s.append((seconds/4))
     

    print (s[0], (s[1] / 2))
    print s

    if(isclose(s[0], s[1])):
        return 'O(1)'
    elif (isclose (s[1], math.log(s[0]) / math.log(10))):
        return 'O(log n)'
    elif(isclose(s[0], (s[1] / 10**2))):
        return 'O(n)'
    elif (isclose (s[0], (s[1] / math.log(s[0]) / math.log(10)))):
        return 'O(n log n)'
    elif(isclose(s[0], (s[1]/ 10**3))):
         return 'O(n^2)'
    else:
        return 'Error'


 




 

 
