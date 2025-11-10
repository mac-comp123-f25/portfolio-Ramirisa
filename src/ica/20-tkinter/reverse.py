import tkinter as tk   # imports the tkinter module so we can make GUI windows, buttons, and text boxes

class ReverseGUI:      # defines a class called ReverseGUI — this is our window and all its parts
    def __init__(self):                        # this runs automatically when we create the window
        self.rootWin = tk.Tk()                 # creates the main window where everything goes
        self.rootWin.title("String Reverser")  # sets the window's title at the top bar

        # --- widgets (the visible parts of the window) ---
        title = tk.Label(self.rootWin, text="Reverse a string", font="Arial 14 bold")
        # creates a text label saying "Reverse a string" in bold font
        title.grid(row=0, column=0, columnspan=2, padx=8, pady=(10, 6))
        # places that label at the top (row 0), stretching across two columns with padding around it

        instr = tk.Label(self.rootWin, text="Type text, then press Enter/Tab:")
        # makes another label giving instructions to the user
        instr.grid(row=1, column=0, sticky="w", padx=8)
        # places it in row 1, column 0, aligned to the left side ("w" for west)

        # Entry and output label must be object variables (self.*)
        self.entry = tk.Entry(self.rootWin, width=40)
        # makes a text box where the user can type something (width 40 characters)
        self.entry.grid(row=1, column=1, padx=8, pady=6)
        # places the text box in row 1, column 1 — next to the instruction label
        self.entry.focus_set()
        # automatically puts the blinking cursor inside the text box when the window opens

        lab = tk.Label(self.rootWin, text="Reversed:")
        # creates another label that says "Reversed:" — this will sit next to the output
        lab.grid(row=2, column=0, sticky="w", padx=8)
        # places it on the left side of row 2, aligned left with padding

        self.output = tk.Label(self.rootWin, text="", font="Consolas 12")
        # creates an empty label (text="") where we’ll show the reversed text later
        # uses a monospace font ("Consolas") so the letters line up evenly
        self.output.grid(row=2, column=1, sticky="w", padx=8)
        # places that label next to "Reversed:" in row 2, column 1

        quit_btn = tk.Button(self.rootWin, text="Quit", command=self.rootWin.destroy)
        # makes a button labeled "Quit" that closes the window when clicked
        quit_btn.grid(row=3, column=0, padx=8, pady=(6, 10), sticky="w")
        # puts the Quit button near the bottom-left corner

        # --- bind callbacks to the Entry ---
        self.entry.bind("<Return>", self.entry_response)
        # tells tkinter to run the entry_response() method when the user presses Enter
        self.entry.bind("<Tab>", self.entry_response)
        # also runs entry_response() when the user presses Tab

    def run(self):
        self.rootWin.mainloop()  # starts the event loop — keeps the window open until closed

    # callback: gets Event object from bind()
    def entry_response(self, event):
        # this method runs automatically when the user presses Enter or Tab
        txt = self.entry.get()        # gets whatever text the user typed into the entry box
        rev = txt[::-1]               # reverses the text (ex: "hello" → "olleh") using slicing
        self.output.config(text=rev)  # updates the output label to show the reversed text
        # Optional: clear the box after using it
        # self.entry.delete(0, tk.END)  # (if you un-comment this, it clears the entry box after pressing Enter)

# --- main program ---
gui = ReverseGUI()  # creates an object of the ReverseGUI class (makes the window)
gui.run()           # runs the program so the window stays open and listens for actions

