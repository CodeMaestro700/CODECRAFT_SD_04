import tkinter as tk
from tkinter import messagebox

# Backtracking Sudoku Solver
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# GUI Interface
class SudokuGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sudoku Solver")
        self.entries = [[None for _ in range(9)] for _ in range(9)]

        for row in range(9):
            for col in range(9):
                e = tk.Entry(master, width=2, font=("Arial", 18), justify="center", borderwidth=2, relief="ridge")
                e.grid(row=row, column=col, padx=3, pady=3)
                self.entries[row][col] = e

        self.solve_button = tk.Button(master, text="Solve", font=("Arial", 14), command=self.solve)
        self.solve_button.grid(row=9, column=0, columnspan=9, pady=10)

        self.load_sample_puzzle()

    def load_sample_puzzle(self):
        sample = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

        for row in range(9):
            for col in range(9):
                if sample[row][col] != 0:
                    self.entries[row][col].insert(0, str(sample[row][col]))

    def solve(self):
        board = []
        try:
            for row in range(9):
                current_row = []
                for col in range(9):
                    val = self.entries[row][col].get()
                    if val == "":
                        current_row.append(0)
                    else:
                        current_row.append(int(val))
                board.append(current_row)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter numbers only.")
            return

        if solve_sudoku(board):
            for row in range(9):
                for col in range(9):
                    self.entries[row][col].delete(0, tk.END)
                    self.entries[row][col].insert(0, str(board[row][col]))
        else:
            messagebox.showinfo("No Solution", "No valid solution exists for the given puzzle.")

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()
