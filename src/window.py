import tkinter as tk

class Window:
    ''' title of the window. '''
    title: str = ""
    window: tk.Tk | None = None

    width = 0
    height = 0

    def __init__(self, width: int, height: int):
        if type(width) is int:
            self.width = width
        if type(height) is int:
            self.height = height

