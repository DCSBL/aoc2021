
with open("input.txt") as file:
    lines = file.readlines()
    
    fishes = [0] * 9
    
    timers = lines[0].split(",")
    for timer in timers:
        fishes[int(timer)] += 1
    
    print(f"Initial: ", end="")
    print(fishes)
    
    for day in range(1, 257):
        print(f"day {str(day).zfill(3)}: ", end="")
        
        # Add new fishes to school
        fishes.append(fishes[0])
        
        # Reset fishes that have counter 0
        fishes[7] += fishes[0]
        
        fishes.pop(0)
        
        print(fishes, end=" = ")
    
        print(sum(fishes))