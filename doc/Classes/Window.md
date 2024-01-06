# Window

Properties:
---

Property           Description
================   ===============================
`title : str`       The title of the window.
`window : tk.Tk`    The tkinter window instance.
`width : int`       The width of the window.
`height : int`      The height of the window.

Methods:
---

### `set_size`:
Sets the size of the window.

Params:
 * `width : int` - The new width of the window ! CANNOT BE `None`!
 * `height : int` - The new height of the window ! CANNOT BE `None`!

Errors:
    `ValueError` -> Happens when either `width` or `height` is `None` or not an integer.

### `display`:
Displays the window.

### `set_title`:
Sets the title of the window.

Params:
 * `new_title : str` - The new title of the window

Errors:
    `ValueError` -> Caused by `new_title` not existing or not being of type `str`.