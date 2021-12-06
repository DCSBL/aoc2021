class Board():
    
    def __init__(self, board):
        self.rows = []
        self.won = False
        for line in board:
            self.rows.append(line.split())
    
    def _check_row(self, row):
        for n in range(5):
            if (self.rows[row][n] != -1):
                return False
        
        return True
            
    def _check_col(self, col):
        for n in range(5):
            if (self.rows[n][col] != -1):
                return False
        
        return True
    
    def mark(self, number):
        for x, row in enumerate(self.rows):
            for y, column in enumerate(row):
                if (int(column) == int(number)):
                    self.rows[x][y] = -1
                    
                    # Something is marked, check if we have bingo..
                    if self._check_row(x) or self._check_col(y):
                        self.won = True
                    
                    return True
        
        return False
    
    def get_sum_of_unmarked(self):
        val = 0
        for row in self.rows:
            for column in row:
                if (int(column) != -1):
                    val += int(column)
                    
        return val
        
    def print_board(self):
        for row in self.rows:
            print(row)
            
        print()
    
    
with open("input.txt") as file:
    lines = file.readlines()
    total_lines = len(lines)
    
    game = lines[0].split(',')
    boards = []
    playing_boards = []
    
    index = 2
    while (index < total_lines):
        board_raw = lines[index + 0: index + 5]
        boards.append(Board(board_raw))
        index += 6
    
    playing_boards = boards
    for number in game:
        print ("Calling number", number)
        boards = playing_boards
        for indx, board in enumerate(boards):
            board.mark(number)
            board.print_board()
            
        for indx, board in enumerate(boards):
            if board.won:
                print("Bingo!")
                board.print_board()
                
                if len(boards) != 1:
                    print("Board won, removing")
                    playing_boards.remove(board)
                    
                else:
                    print("Found last bingo")
                    marked = board.get_sum_of_unmarked()
                    print(marked, "*", number, "=", marked*int(number))
                    exit()