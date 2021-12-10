with open("input.txt") as file:
    lines = file.readlines()
    
    entries = []
    
    # Load
    for line in lines:
        entry = line.split(" | ")
        entry = [sorted(entry[0].split(), key=len), entry[1].split()]
        # print(entry)
        entries.append(entry)
    
    m = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6}
    
    
    
    def chars_in_string(chars, string):
        for char in chars:
            if char not in string:
                return False
                
        return True
        
    def decode(digits, number):
        s_number = sorted(number)
        for indx, digit in enumerate(digits):
            if (sorted(digit) == s_number):
                return indx
                
        assert False
    
    total_number = 0
    
    for entry in entries:
        digits = [''] * 10
        
        for indx, digit in enumerate(entry[0]):
                    
            if len(digit) == 2:
                digits[1] = digit
                entry[0][indx] = ""
                
            if len(digit) == 4:
                digits[4] = digit
                entry[0][indx] = ""
                
            if len(digit) == 3:
                digits[7] = digit
                entry[0][indx] = ""
                
            if len(digit) == 7:
                digits[8] = digit
                entry[0][indx] = ""
        
        
        for indx, digit in enumerate(entry[0]):
            
            if len(digit) == 5: # Can be 2, 3, 5
                if chars_in_string(digits[7],digit): # 7 should fit in 3, not 2 and 5
                    digits[3] = digit
                    entry[0][indx] = ""
                    
            if len(digit) == 6: # Can be 0, 6, 9
                if chars_in_string(digits[4],digit): # 4 should fit in 9, not 0 and 9
                    digits[9] = digit
                    entry[0][indx] = ""
        
        
        for indx, digit in enumerate(entry[0]):
            
            if len(digit) == 6: # Can be 0, 6
                if chars_in_string(digits[1],digit): # 1 should fit in 0, not 6
                    digits[0] = digit
                    entry[0][indx] = ""
                    
        for indx, digit in enumerate(entry[0]):
            
            if len(digit) == 6: # Can be 6
                digits[6] = digit
                entry[0][indx] = ""
        
        for indx, digit in enumerate(entry[0]):
            
            if len(digit) == 5: # Can be 2, 5
                if chars_in_string(digit, digits[6]): # 5 should fit in 6, 2 should not fit
                    digits[5] = digit
                    entry[0][indx] = ""     
                    
        for indx, digit in enumerate(entry[0]):
            
            if len(digit) == 5: # Can be 2
                digits[2] = digit
                entry[0][indx] = ""
            
        code = ""
        for number in entry[1]:
            code += str(decode(digits, number))
        
        total_number += int(code)
        print(code)
        
    print(total_number)