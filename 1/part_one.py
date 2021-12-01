
with open("input.txt") as file:
    lines = file.readlines()
    
    higher_than_previous = 0
    
    previous = -1
    
    for line in lines:
        number = (int(line))
        
        if number > previous and previous != -1:
            higher_than_previous += 1
        
        previous = number
        
    print(higher_than_previous)