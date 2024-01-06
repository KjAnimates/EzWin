import tkinter as tk

class Window:
    ''' title of the window. '''
    title: str = ""
    window: tk.Tk | None = None

    # The dimensions of the window
    width: int  = 0
    height: int = 0

    def __init__(self, width: int, height: int):
        # Check If <dimension> isn't `None`, and it is an integer
        if width != None and type(width) is int:
            self.width = width
        if height != None and type(height) is int:
            self.height = height
