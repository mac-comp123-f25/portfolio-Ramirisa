import tkinter as tk   # imports the tkinter module and shortens its name to tk

class MoveTextGUI:     # defines a class (blueprint) for the GUI program
    def __init__(self):                        # this runs when the program starts
        # --- main window ---
        self.rootWin = tk.Tk()                 # creates the main window
        self.rootWin.title("Canvas Move Demo") # sets the window’s title text

        # Optional header + quit button (outside the canvas)
        tk.Label(self.rootWin, text="Use W/A/S/D or Arrow Keys to move the text").grid(
            row=0, column=0, columnspan=2, padx=8, pady=(8, 4), sticky="w"
        )
        # creates a label at the top with instructions for the user

        tk.Button(self.rootWin, text="Quit", command=self.rootWin.destroy).grid(
            row=0, column=1, padx=8, pady=(8, 4), sticky="e"
        )
        # creates a "Quit" button that closes the window when clicked

        # --- Canvas (object variable) ---
        self.canvas = tk.Canvas(self.rootWin, width=500, height=300, bg="#e6f2ff", bd=2, relief=tk.SUNKEN)
        # creates a drawing area (Canvas) with width 500, height 300, light blue background
        # bd=2 gives it a border, and relief=tk.SUNKEN makes it look slightly inset
        self.canvas.grid(row=1, column=0, columnspan=2, padx=8, pady=8)
        # places the canvas in the window (row 1), with padding and spanning both columns

        # --- Text object (store its ID) ---
        # Replace "Your Name" with your name
        self.text_id = self.canvas.create_text(250, 150, text="Your Name", fill="darkblue", font="Arial 16 bold")
        # draws your name as text on the canvas at coordinates (250, 150)
        # stores the text’s ID number in self.text_id so we can move it later

        # --- Key bindings on the MAIN WINDOW (not the canvas) ---
        # WASD
        self.rootWin.bind("<KeyPress-w>", self.move_callback)
        self.rootWin.bind("<KeyPress-a>", self.move_callback)
        self.rootWin.bind("<KeyPress-s>", self.move_callback)
        self.rootWin.bind("<KeyPress-d>", self.move_callback)
        # these lines say: when the user presses w/a/s/d, call move_callback()

        # Arrows
        self.rootWin.bind("<Up>", self.move_callback)
        self.rootWin.bind("<Left>", self.move_callback)
        self.rootWin.bind("<Down>", self.move_callback)
        self.rootWin.bind("<Right>", self.move_callback)
        # same as above, but for the arrow keys

        # Ensure the window has focus to receive key presses
        self.rootWin.focus_set()  # makes sure the window is ready to detect key presses

    def run(self):
        self.rootWin.mainloop()  # keeps the window open and waiting for user actions

    # --- Callback: receives an Event object ---
    def move_callback(self, event):       # function that runs when a key is pressed
        key = event.keysym                # stores the name of the key pressed (like 'w' or 'Up')
        # print(key)                      # (you could uncomment this to test what key names look like)

        dx, dy = 0, 0                     # dx and dy represent how far to move in x and y direction
        step = 10                         # each movement will be 10 pixels

        # Move up
        if key in ("w", "Up"):            # if 'w' or the Up arrow key was pressed
            dy = -step                    # move upward by 10 pixels (negative y)
        # Move left
        elif key in ("a", "Left"):        # if 'a' or the Left arrow key was pressed
            dx = -step                    # move left by 10 pixels (negative x)
        # Move down
        elif key in ("s", "Down"):        # if 's' or the Down arrow key was pressed
            dy = step                     # move down by 10 pixels
        # Move right
        elif key in ("d", "Right"):       # if 'd' or the Right arrow key was pressed
            dx = step                     # move right by 10 pixels

        # only move if there’s actually a direction change
        if dx != 0 or dy != 0:
            self.canvas.move(self.text_id, dx, dy)  # moves the text by (dx, dy) pixels on the canvas

# --- Main program ---
app = MoveTextGUI()  # creates the window (calls __init__)
app.run()            # starts the program so the window appears and runs until closed


