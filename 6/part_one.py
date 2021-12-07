class Fish():
    
    timer = 0
    
    def __init__(self, timer):
        self.timer = int(timer)
        
    def __str__(self) -> str:
        return str(self.timer)
    
    def tick(self):
        self.timer -= 1
        if (self.timer == -1):
            self.timer = 6
            return True
            
        return False
    
with open("input.txt") as file:
    lines = file.readlines()
    
    fishes = []
    
    timers = lines[0].split(",")
    for timer in timers:
        fishes.append(Fish(timer))
    
    for day in range(1, 81):
        print(f"day {str(day).zfill(2)}: ", end="")
        
        new_fishes = []
        
        for fish in fishes:
            if fish.tick():
                new_fishes.append(Fish(8))
            print(fish, end=",")
        
        for fish in new_fishes:
            fishes.append(fish)
            print(fish, end=",")
        
        print("")
        
    print(len(fishes))