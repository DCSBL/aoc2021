import numpy as np

COORD_X = 0
COORD_Y = 1
SIZE_W = 0
SIZE_H = 1

class Grid():
    
    grid = []
        
    def set_size(self, width, height):
        self.grid = []
        for row in range(height):
            self.grid.append([])
        
            for col in range(width):
                self.grid[row].append(0)
    
    def get_size(self):
        width = len(self.grid)
        if (width == 0):
            height = 0 
        else:
            height = len(self.grid[0])
        return (width, height)
        
    def print_grid(self):
        for row in self.grid:
            print(row)
        
        print()
        
    def calc_grid(self):
        overlap = 0
        for row in self.grid:
            for col in row:
                if (col >= 2):
                    overlap += 1
        
        return overlap
        
    
    def draw_line(self, start, end):
        if (start[COORD_X] == end[COORD_X]):
            # Going horizonal
            print("Horizonal line", start, end)
            if (start[COORD_X] > end[COORD_X]):
                temp = start[COORD_X]
                start[COORD_X] = end[COORD_X]
                end[COORD_X] = temp
            
            if (start[COORD_Y] > end[COORD_Y]):
                temp = start[COORD_Y]
                start[COORD_Y] = end[COORD_Y]
                end[COORD_Y] = temp
            
            for y in range(start[COORD_Y], end[COORD_Y] + 1):
                # print("Hor", y)
                self.grid[y][start[COORD_X]] += 1
        
        elif (start[COORD_Y] == end[COORD_Y]):
            # Going vertical
            print("Vertical line", start, end)
            if (start[COORD_X] > end[COORD_X]):
                temp = start[COORD_X]
                start[COORD_X] = end[COORD_X]
                end[COORD_X] = temp
            
            if (start[COORD_Y] > end[COORD_Y]):
                temp = start[COORD_Y]
                start[COORD_Y] = end[COORD_Y]
                end[COORD_Y] = temp
                
            for x in range(start[COORD_X], end[COORD_X] + 1):
                # print("ver", x, start[COORD_Y])
                self.grid[start[COORD_Y]][x] += 1
                
        else:
            go_right =  (start[COORD_X] < end[COORD_X])
            go_down = (start[COORD_Y] < end[COORD_Y])
            
            coord_current = start
            while (coord_current != end):
                self.grid[coord_current[COORD_Y]][coord_current[COORD_X]] += 1
                if (go_right):
                    coord_current[COORD_X] += 1
                else:
                    coord_current[COORD_X] -= 1
                    
                if (go_down):
                    coord_current[COORD_Y] += 1
                else:
                    coord_current[COORD_Y] -= 1
                    
            self.grid[coord_current[COORD_Y]][coord_current[COORD_X]] += 1
    
    def add_line(self, line):
        coord = self.get_coord_from_line(line)
        print("Drawing line", coord)
        self.draw_line(coord[0], coord[1])
        
    def get_coord_from_line(self, line):
        line = line.strip().split(" -> ")
        start = line[0].split(",")
        end =   line[1].split(",")
        start[COORD_X] = (int(start[COORD_X]))
        start[COORD_Y] = (int(start[COORD_Y]))
        end[COORD_X] = (int(end[COORD_X]))
        end[COORD_Y] = (int(end[COORD_Y]))
        
        return (start, end)
        
        
with open("input.txt") as file:
    lines = file.readlines()
    
    grid = Grid()
    
    width = 0
    height = 0
        
    grid.set_size(1000, 1000)
        
    for line in lines:
        grid.add_line(line)
    
    grid.print_grid()
    print(grid.calc_grid())