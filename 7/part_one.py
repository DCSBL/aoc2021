
with open("input.txt") as file:
    lines = file.readlines()
    
    crabs = list(map(int, lines[0].split(',')))
    crabs.sort()
    
    lowest_fuel = 999999
    
    for indx in range(len(crabs)):
        fuel = 0
        
        for crab in crabs:
            fuel += abs(indx - crab)
            
        if (fuel < lowest_fuel):
            lowest_fuel = fuel
            
        # print(fuel)
            
    print(lowest_fuel)