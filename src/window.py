class Window:
    ''' title of the window. '''
    title: str = ""

    def __init__(self, title: str):
        if title != None and title is str:
            self.title = title
