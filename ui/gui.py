import tkinter as tk
from controller.autocomplete_controller import AutocompleteController
from utils.file_loader import load_words_from_file

class AutocompleteGUI:
    def __init__(self, root):
        self.controller = AutocompleteController()

        # Load words
        try:
            for word in load_words_from_file("data/words.txt"):
                self.controller.add_word(word)
        except FileNotFoundError:
            pass  # fallback if file doesn't exist

        self.root = root
        self.root.title("Autocomplete App")

        self.entry = tk.Entry(root, font=("Arial", 14), width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<KeyRelease>", self.update_suggestions)

        self.listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
        self.listbox.pack()

    def update_suggestions(self, event):
        prefix = self.entry.get()
        self.listbox.delete(0, tk.END)

        if prefix:
            suggestions = self.controller.get_suggestions(prefix)
            for suggestion in suggestions:
                self.listbox.insert(tk.END, suggestion)
