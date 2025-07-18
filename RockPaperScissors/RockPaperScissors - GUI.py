import random
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk

def Rules(Choice, Computer):
    if Choice == Computer:
        return "Tie"
    elif Choice == "ROCK":
        return "Lose" if Computer == "PAPER" else "Win"
    elif Choice == "PAPER":
        return "Lose" if Computer == "SCISSORS" else "Win"
    elif Choice == "SCISSORS":
        return "Win" if Computer == "PAPER" else "Lose"


window = ttk.Window(themename="minty")  
window.title("RockPaperScissors")
window.geometry('900x800')
window.configure(bg="#f4e3b2")
style = ttk.Style()
style.configure("CustomFrame.TFrame", background="#f4e3b2")


rock_img = ImageTk.PhotoImage(Image.open("rock.png").resize((120, 120)))
paper_img = ImageTk.PhotoImage(Image.open("paper.png").resize((120, 120)))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png").resize((120, 120)))


ttk.Label(window, text="PLAY ROCK PAPER SCISSORS!",
          font=("Arial", 28, "bold"), foreground="#5e1104", background="#f4e3b2").pack(pady=20)



points_frame = ttk.LabelFrame(window, text="POINT SYSTEM", bootstyle="danger", padding=10)
points_frame.pack(pady=10)
ttk.Label(points_frame, text="Win: +1\nLose: +1 to Computer\nTie: 0",
          font=("Arial", 16), foreground="#5e1104", background="#f4e3b2", justify="left").pack()



image_frame = ttk.Frame(window, padding=10, style="CustomFrame.TFrame")
image_frame.pack(pady=10)

player_image_label = ttk.Label(image_frame)
player_image_label.config(image=rock_img)
player_image_label.image = rock_img  
player_image_label.grid(row=0, column=0, padx=20)

computer_image_label = ttk.Label(image_frame)
computer_image_label.config(image=paper_img)
computer_image_label.image = paper_img  
computer_image_label.grid(row=0, column=1, padx=20)


radio_var = ttk.StringVar(value="ROCK")
radio_frame = ttk.Frame(window, padding=10, style="CustomFrame.TFrame")
radio_frame.pack(pady=10)

choices = ["ROCK", "PAPER", "SCISSORS"]
for choice in choices:
    ttk.Radiobutton(radio_frame, text=choice, variable=radio_var, value=choice,
                    bootstyle="info", style="Toolbutton").pack(side="left", padx=15)


Player_Points = 0
Computer_Points = 0

def game_start():
    global Player_Points, Computer_Points
    hand = radio_var.get()
    Computer = random.choice(choices)
    messagebox.showinfo("Computer's Move", f"Computer chose {Computer.title()}")

    def update_images(player_choice, computer_choice):
        image_map = {"ROCK": rock_img, "PAPER": paper_img, "SCISSORS": scissors_img}
        player_image_label.config(image=image_map[player_choice])
        player_image_label.image = image_map[player_choice]  

        computer_image_label.config(image=image_map[computer_choice])
        computer_image_label.image = image_map[computer_choice] 

    update_images(hand, Computer)
    Result = Rules(hand, Computer)

    if Result == "Win":
        Player_Points += 1
        messagebox.showinfo("Round Result", "You won this round! +1 point to you.")
    elif Result == "Lose":
        Computer_Points += 1
        messagebox.showinfo("Round Result", "You lost this round! +1 point to computer.")
    else:
        messagebox.showinfo("Round Result", "It's a tie! No points.")

    play_again = simpledialog.askstring("Continue?", "Do you want to play another round? Y/N")
    if not play_again or play_again.upper() != "Y":
        show_final_result()

result_label = ttk.Label(window, text="", font=("Arial", 28, "bold"),
                         foreground="#5e1104", background="#f4e3b2")
result_label.pack(pady=10)

def show_final_result():
    global Player_Points, Computer_Points
    messagebox.showinfo("Final Result", f"You: {Player_Points} | Computer: {Computer_Points}")
    if Player_Points > Computer_Points:
        result_label.config(text="YOU WON!!", foreground="#45462A")
    elif Computer_Points > Player_Points:
        result_label.config(text="COMPUTER WON!!", foreground="#5e1101")
    else:
        result_label.config(text="IT'S A TIE!", foreground="#25344f")


style.configure("Custom.Outline.TButton", font=("Arial", 14, "bold"),
                foreground="#5e1104", bordercolor="#7f8330", relief="solid",
                borderwidth=2, padding=10)

submit_btn = ttk.Button(window, text="Submit", style="Custom.Outline.TButton", command=game_start)
submit_btn.pack(pady=20)

window.mainloop()
