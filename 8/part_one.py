
with open("input.txt") as file:
    lines = file.readlines()
    
    entries = []
    
    # Load
    for line in lines:
        entry = line.split(" | ")
        entry = [entry[0].split(), entry[1].split()]
        print(entry)
        entries.append(entry)
    
    digits = [0] * 10
    
    for entry in entries:
        for digit in entry[1]:
            if len(digit) == 2:
                digits[1] += 1
                
            if len(digit) == 4:
                digits[4] += 1
                
            if len(digit) == 3:
                digits[7] += 1
                
            if len(digit) == 7:
                digits[8] += 1
                
    print(sum(digits))