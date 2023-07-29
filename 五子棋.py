import tkinter as tk
from tkinter import messagebox

BOARD_SIZE = 15
CELL_SIZE = 103

class GomokuGame:
    def __init__(self):
        self.board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.current_player = 'X'
        self.winner = None

    def make_move(self, row, col):
        if self.winner or self.board[row][col] != ' ':
            return

        self.board[row][col] = self.current_player
        if self.check_win(row, col):
            self.winner = self.current_player
        else:
            self.current_player = 'X' if self.current_player == 'O' else 'O'

    def check_win(self, row, col):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            for i in range(1, 5):
                r, c = row + dr * i, col + dc * i
                if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and self.board[r][c] == self.board[row][col]:
                    count += 1
                else:
                    break
            for i in range(1, 5):
                r, c = row - dr * i, col - dc * i
                if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and self.board[r][c] == self.board[row][col]:
                    count += 1
                else:
                    break
            if count >= 5:
                return True
        return False

class GomokuGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gomoku")
        self.game = GomokuGame()

        self.canvas = tk.Canvas(self.root, width=BOARD_SIZE * CELL_SIZE, height=BOARD_SIZE * CELL_SIZE, bg="#e0c090")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)

        self.draw_board()

    def draw_board(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                x, y = col * CELL_SIZE, row * CELL_SIZE
                self.canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, outline="#78552b", fill="#e0c090")
                if self.game.board[row][col] != ' ':
                    color = "black" if self.game.board[row][col] == 'X' else "white"
                    self.canvas.create_oval(x + 5, y + 5, x + CELL_SIZE - 5, y + CELL_SIZE - 5, fill=color)

    def on_click(self, event):
        if not self.game.winner:
            col, row = event.x // CELL_SIZE, event.y // CELL_SIZE
            self.game.make_move(row, col)
            self.canvas.delete("all")
            self.draw_board()
            if self.game.winner:
                self.show_winner()

    def show_winner(self):
        winner = "Player X" if self.game.winner == 'X' else "Player O"
        messagebox.showinfo("Game Over", f"{winner} wins!")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = GomokuGUI()
    gui.run()
