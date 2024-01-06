import tkinter as tk

class Window:
    ''' title of the window. '''
    title: str = "Untitled Window"
    window: tk.Tk | None = None

    # The dimensions of the window
    width: int  = 0
    height: int = 0

    def __init__(self, width: int = 0, height: int = 0):
        self.window = tk.Tk()
        self.window.title(self.title)

        # Check If <dimension> isn't `None`, and it is an integer
        if width != None and type(width) is int:
            self.width = width
        if height != None and type(height) is int:
            self.height = height
    
    ''' Sets the size of the window
    @param width: The new width of the window   ! CANNOT BE `None`!
    @param height: The new height of the window ! CANNOT BE `None`!

    Errors:
        `ValueError` -> Happens when either `width` or `height` is `None` or not an integer.
    '''
    def set_size(self, width: int, height: int):
        if width != None and type(width) is int:
            self.width = width
        else:
            raise ValueError("Width must be an integer and must not be `None`.")
        
        if height != None and type(height) is int:
            self.height = height
        else:
            raise ValueError("Height must be an integer and must not be `None`.")
    
    ''' Displays the window. '''
    def display(self):
        if self.window != None:
            self.window.mainloop()
        else:
            print("WARNING: Window did not open since it does not exist.")
