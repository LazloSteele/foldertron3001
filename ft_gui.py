from tkinter import *
from tkinter import filedialog
import observer
import os
import foldertron3002 as ft

class browser():
    def __init__(self):
        self.root = Tk()
        self.root.title('File Explorer')        
        self.root.geometry("700x500")
        self.root.config(background = "white")

        self._dir = StringVar()
        self._file = StringVar()
        self._header_label = Label(self.root, text = "LMP Foldertron 3001", width = 100, height = 4, fg = "black")
        self._dir_label = Label(self.root, text = f"Current Directory: {self._dir.get()}", width = 100, height = 1, fg = "blue")
        self._file_label = Label(self.root, text = f"Current Schedule: {self._file.get()}", width = 100, height = 1, fg = "blue")
        self._dir_state = observer.data_class("Current Working Directory")
        self._file_state = observer.data_class("Schedule File")

        self._button_explore = Button(self.root, text = "Browse Files", command = self.browse_files)
        self._button_directory = Button(self.root, text = "Choose Directory", command = self.browse_folders)
        self._button_go = Button(self.root, text = "Go", command = self.go)
        self._button_exit = Button(self.root, text = "Exit", command = exit)
        self._status_text = Text(self.root, height = 10, width = 52)

        self._header_label.grid(column = 1, row = 1)
        self._file_label.grid(column = 1, row = 2)
        self._dir_label.grid(column = 1, row = 3)
        self._button_explore.grid(column = 1, row = 4)
        self._button_directory.grid(column = 1, row = 5)
        self._button_go.grid(column = 1, row = 6)
        self._button_exit.grid(column = 1, row = 7)
        self._status_text.grid(column = 1, row = 8)

        self.set_observers()

    def go(self):
        ft.parse_excel(self._file_state.data, self._dir_state.data)
        
    def set_observers(self):
        self._dir_state.data = os.getcwd()
        self._file_state.data = "None"

    def update(self):
        self._dir.set(self._dir_state.data)
        self._file.set(self._file_state.data)
        self._dir_label.config(text = f"Current Directory: {self._dir.get()}")
        self._file_label.config(text = f"Current File: {self._file.get()}")
        
    def browse_files(self):
        filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Spreadsheet files", "*.xlsx"), ("all files", "*.*")))

        self._file_state.data = filename
        self.update()

    def browse_folders(self):
        directory_name = filedialog.askdirectory()
        
        self._dir_state.data = directory_name
        self.update()

    def post_message(self, message):
        self._status_text.insert(tkinter.END, message)
