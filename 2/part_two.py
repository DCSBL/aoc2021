
with open("input.txt") as file:
    lines = file.readlines()
    
    hor = 0
    depth = 0
    aim = 0
    
    for line in lines:
        instruction = str.split(line)
        direction = instruction[0]
        steps = int(instruction[1])
        
        if (direction == "forward"):
            hor = hor + steps
            aim = aim + (depth * steps)
        elif (direction == "up"):
            depth = depth - steps
        elif (direction == "down"):
            depth = depth + steps
        
    print(f"hor ({hor}) * aim ({aim}) = {hor*aim}")
