
with open("input.txt") as file:
    lines = file.readlines()
    
    # Prepare commons array
    bitwidth = len(lines[0]) - 1
    common = [0] * bitwidth
    
    # Get hightes
    for line in lines:
        for indx, letter in enumerate(line):
            if letter == '1':
                value = int(line)
                common[indx] += 1
    
    # Get value number
    gamma = ''
    epsilon = ''
    half_lines = len(lines) / 2
    
    for index, value in enumerate(common):
        if (value > half_lines):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
            
    gamma_num = int(gamma, 2)
    epsilon_num = int(epsilon, 2)
    
    print(gamma_num * epsilon_num)