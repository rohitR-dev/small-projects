import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                                   command=lambda r=row, c=col: self.button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def button_click(self, row, col):
        if self.buttons[row][col].cget("text") == "":
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif all(self.buttons[r][c].cget("text") != "" for r in range(3) for c in range(3)):
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check rows
        for row in range(3):
            if self.buttons[row][0].cget("text") == self.buttons[row][1].cget("text") == self.buttons[row][2].cget("text") != "":
                return True
        # Check columns
        for col in range(3):
            if self.buttons[0][col].cget("text") == self.buttons[1][col].cget("text") == self.buttons[2][col].cget("text") != "":
                return True
        # Check diagonals
        if self.buttons[0][0].cget("text") == self.buttons[1][1].cget("text") == self.buttons[2][2].cget("text") != "":
            return True
        if self.buttons[0][2].cget("text") == self.buttons[1][1].cget("text") == self.buttons[2][0].cget("text") != "":
            return True
        return False

    def reset_game(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
