
with open("input.txt") as file:
    lines = file.readlines()
    
    higher_than_previous = 0
    previous_sum = 0
    
    items = []
    
    for line in lines:
        number = (int(line))
        
        items.append(number)
        
        if (len(items) > 3):
            items = items[1:]
            current_sum = sum(items)
            
            if (current_sum > previous_sum):
                higher_than_previous += 1
                print(items, current_sum, "increased")
            else:
                print(items, current_sum, "-")
            
            previous_sum = current_sum
        
    print(higher_than_previous)