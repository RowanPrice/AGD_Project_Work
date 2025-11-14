import tkinter as tk


class ClickApp(tk.Tk):
    """ Button clicker application """

    def __init__(self):
        # Initialised the tk.Tk app superclass
        super().__init__()

        self.title('Click Counter')
        self.clicker_frame = ButtonClicker(self)
        self.clicker_frame.pack(side=tk.LEFT)


class ButtonClicker(tk.Frame):
    """ Frame with button clicker widgets """

    def __init__(self, master):
        super().__init__(master)

    def place_widgets(self):
        ...


if __name__ == '__main__':
    app = ClickApp()
    app.mainloop()