# Window

Properties:
---
 * `title : str`    ->   The title of the window.
 * `window : tk.Tk` ->   The tkinter window instance.
 * `width : int`    ->   The width of the window.
 * `height : int`   ->   The height of the window.

Methods:
---

### `set_size(width: int, height: int)`:
Sets the size of the window.

Params:
 * `width : int` - The new width of the window
                   ! CANNOT BE `None`!
 * `height : int` - The new height of the window
                    ! CANNOT BE `None`!

Errors:
    `ValueError` -> Happens when either `width` or `height` is `None` or not an integer.

### `display()`:
Displays the window.

### `set_title(new_title: str)`:
Sets the title of the window.

Params:
 * `new_title : str` - The new title of the window

Errors:
    `ValueError` -> Caused by `new_title` not existing or not being of type `str`.

### `set_geometry(new_geometry: str)`:
Sets the geometry of the window.

Params:
 * `new_geometry` - The new geometry of the window (`width`x`height`)