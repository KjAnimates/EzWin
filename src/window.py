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
    
    def set_size(self, width: int, height: int):
        if width != None and type(width) is int:
            self.width = width
        else:
            raise ValueError("Width must be an integer and must not be `None`.")
        
        if height != None and type(height) is int:
            self.height = height
        else:
            raise ValueError("Height must be an integer and must not be `None`.")
