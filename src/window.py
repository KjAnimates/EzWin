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
            self.window.title(self.title)
            self.window.mainloop()
        else:
            print("WARNING: Window did not open since it does not exist.")
    
    ''' Sets the title of the window.
    @param new_title: The new title of the window

    Errors:
        `ValueError` -> Caused by `new_title` not existing or not being of type `str`.
    '''
    def set_title(self, new_title: str = "Untitled Window"):
        if new_title != None:
            if type(new_title) is str:
                self.title = new_title
            else:
                raise ValueError("Parameter #1 (`new_title: str`) must exist and be of type 'str'.")
    
    ''' Sets the geometry of the window.
    @param new_geometry: The new geometry of the window (`width`x`height`)
    '''
    def set_geometry(self, new_geometry: str):
        if new_geometry != None:
            if type(new_geometry) is str:
                self.window.geometry(new_geometry)

