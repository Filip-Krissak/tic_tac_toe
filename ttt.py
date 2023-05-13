import tkinter as tk
from tkinter import messagebox

current_player = "X"
board = [[" " for _ in range(3)] for _ in range(3)]
buttons = []

def click_button(row, col):
    global current_player
    if buttons[row][col]["text"] == " ":
        buttons[row][col]["text"] = current_player
        board[row][col] = current_player
        if check_win():
            messagebox.showinfo("Tic Tac Toe", f"{current_player} wins!")
            reset_game()
        elif check_tie():
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

def check_win():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        elif board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    elif board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def check_tie():
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def reset_game():
    global current_player
    current_player = "X"
    global board
    board = [[" " for _ in range(3)] for _ in range(3)]
    for row in buttons:
        for button in row:
            button["text"] = " "

root = tk.Tk()
root.title("Tic Tac Toe")

for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(root, text=" ", font=("Helvetica", 20),
                           width=5, height=2, command=lambda row=row, col=col: click_button(row, col))
        button.grid(row=row, column=col, sticky="nsew")
        button_row.append(button)
    buttons.append(button_row)

reset_button = tk.Button(root, text="Reset", font=("Helvetica", 20),
                         width=5, height=2, command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

root.mainloop()
