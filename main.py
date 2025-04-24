import tkinter as tk
from ui.gui import AutocompleteGUI

def main():
    root = tk.Tk()
    app = AutocompleteGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
