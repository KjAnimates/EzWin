import tkinter as tk

class Window:
    ''' title of the window. '''
    title: str = ""
    window: tk.Tk | None = None

    def __init__(self, title: str):
        if title != None and title is str:
            self.title = title
