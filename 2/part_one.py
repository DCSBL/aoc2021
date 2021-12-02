
with open("input.txt") as file:
    lines = file.readlines()
    
    hor = 0
    ver = 0
    
    for line in lines:
        instruction = str.split(line)
        direction = instruction[0]
        steps = int(instruction[1])
        
        if (direction == "forward"):
            hor = hor + steps
        elif (direction == "up"):
            ver = ver - steps
        elif (direction == "down"):
            ver = ver + steps
        
    print(f"hor ({hor}) * ver ({ver}) = {hor*ver}")
