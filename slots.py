import tkinter as tk
import random

class SlotMachine:
    def __init__(self):
        self.symbols = ["🍒", "🍋", "🍊", "🍉", "⭐", "💎"]
        self.reels = 3  # Number of reels

    def spin(self):
        return [random.choice(self.symbols) for _ in range(self.reels)]

class SlotGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Slot Machine Game")
        self.root.geometry("400x500")  # Set initial window size
        self.root.resizable(False, False)  # Disable resizing
        self.root.config(bg="#2C3E50")  # Set background color

        # Initialize the SlotMachine
        self.machine = SlotMachine()
        self.points = 369  # Starting points

        # Frame for results
        self.result_frame = tk.Frame(root, bg="#34495E", padx=20, pady=20)
        self.result_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=(10, 0))

        self.result_label = tk.Label(self.result_frame, text="Press 'Spin' to start!", font=("Helvetica", 20), bg="#34495E", fg="white")
        self.result_label.pack(pady=(10, 5))

        self.reel_display = tk.Label(self.result_frame, text="", font=("Helvetica", 48), bg="#34495E", fg="white")
        self.reel_display.pack(pady=5)

        # Frame for points display
        self.points_frame = tk.Frame(root, bg="#2C3E50")
        self.points_frame.pack(pady=(10, 20))

        self.points_label = tk.Label(self.points_frame, text=f"Points: {self.points}", font=("Helvetica", 18), bg="#2C3E50", fg="white")
        self.points_label.pack(pady=10)

        # Frame for the button
        self.button_frame = tk.Frame(root, bg="#2C3E50")
        self.button_frame.pack(pady=(10, 20))

        self.spin_button = tk.Button(self.button_frame, text="Spin", command=self.spin, font=("Helvetica", 18), bg="green", fg="white", padx=20, pady=10)
        self.spin_button.pack(pady=10)

        # Center align the frames
        self.result_frame.pack_propagate(False)  # Prevents the frame from resizing to fit its contents
        self.result_frame.config(width=360, height=200)  # Adjust frame size to fit content

    def spin(self):
        if self.points > 0:  # Check if the user has points to spin
            spin_result = self.machine.spin()  # Correctly reference self.machine
            self.reel_display.config(text=" ".join(spin_result))
            self.points -= 1  # Deduct 1 point for the spin
            self.points_label.config(text=f"Points: {self.points}")  # Update points display
            
            if self.check_winner(spin_result):
                self.points += 100  # Add 100 points for a win
                self.result_label.config(text="Congratulations! You won!")
            else:
                self.result_label.config(text="Sorry, you lost. Try again!")
        else:
            self.result_label.config(text="No points left! Please restart the game.")

    def check_winner(self, spin_result):
        # Check if all symbols are the same
        return len(set(spin_result)) == 1

if __name__ == "__main__":
    root = tk.Tk()
    game = SlotGame(root)
    root.mainloop()
