class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0]*n for i in range(n)]
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        def check_for_winner(row, col, player):
            #check for row
            if all(self.board[i][col] == player for i in range(self.n)):
                return player
            
            #check for col
            if all(self.board[row][i] == player for i in range(self.n)):
                return player
                
            #check for diagonal
            if row == col and all(self.board[i][i] == player for i in range(self.n)):
                return player
                
            if row == (self.n - col - 1) and all(self.board[i][self.n - i - 1] == player for i in range(self.n)):

                return player
            
            return 0
            
        return check_for_winner(row, col, player)
