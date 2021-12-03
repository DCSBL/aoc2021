
with open("input.txt") as file:
    lines = file.readlines()
    
    bitwidth = len(lines[0]) - 1
    worklist = lines
    
    oxygen = 0
    co2 = 0
    
    for index in range(bitwidth):
        worklist_ones = []
        worklist_zero = []
        
        # Get hightes
        for line in worklist:
            if line[index] == '1':
                worklist_ones.append(line)
            else:
                worklist_zero.append(line)
        
        if (len(worklist_ones) >= len(worklist_zero)):
            worklist = worklist_ones
        else:
            worklist = worklist_zero
            
        if (len(worklist) == 1):
            oxygen = int(worklist[0], 2)
            break
        
    worklist = lines
    
    for index in range(bitwidth):
        worklist_ones = []
        worklist_zero = []
        
        # Get hightes
        for line in worklist:
            if line[index] == '1':
                worklist_ones.append(line)
            else:
                worklist_zero.append(line)
        
        if (len(worklist_ones) < len(worklist_zero)):
            worklist = worklist_ones
        else:
            worklist = worklist_zero
            
        if (len(worklist) == 1):
            co2 = int(worklist[0], 2)
            break
        
    print(oxygen * co2)