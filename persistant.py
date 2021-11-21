from functools import reduce

def persistence(n):
    if n <= 9: 
        return 0
    
    else:
        
        times = 0

        while n > 9:            
            n = reduce(lambda x, y: x * y, map(int, str(n)))
            times += 1

        return times
