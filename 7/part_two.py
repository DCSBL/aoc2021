import sys

with open("input.txt") as file:
    lines = file.readlines()
    
    crabs = list(map(int, lines[0].split(',')))
    crabs.sort()
    
    lowest_fuel = -1
    
    sys.setrecursionlimit(10000)
    def steps(step):
        if (step == 0):
            return 0
            
        return step + steps(step - 1)
    
    print("This one takes a while..")
    
    for indx in range(len(crabs)):
        fuel = 0
        
        for crab in crabs:
            fuel += steps(abs(indx - crab))
        
        print(fuel)
        
        if (fuel < lowest_fuel or lowest_fuel == -1):
            lowest_fuel = fuel
        else:
            print("Lowest is", lowest_fuel)
            break