import tkinter as tk


class ClickApp(tk.Tk):
    """ Button clicker application """

    def __init__(self):
        # Initialised the tk.Tk app superclass
        super().__init__()
        self.title('Click Counter')
        self.clicker_frame = ButtonClicker(self)
        self.background_colour_frame = BackgroundColorFrame(self)

        self.clicker_frame.pack(side=tk.LEFT)
        self.background_colour_frame.pack(side=tk.LEFT)


class ButtonClicker(tk.Frame):
    """ Frame with button clicker widgets """

    def __init__(self, master):
        super().__init__(master)
        self.counter = 0

        self.btn = tk.Button(self, text="Do not press", bg="red", fg="black", activebackground="black",activeforeground="red", command=self.click_button)
        self.response_txt = tk.Label(self, text="No Clicks")

        self.place_widgets()


    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10, 'sticky': 'nswe'}
        self.btn.grid(row=1, column=0, **settings)
        self.response_txt.grid(row=1, column=1, **settings)

    def click_button(self):
        self.counter += 1
        self.response_txt.config(text=self.counter)


class BackgroundColorFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Color choices
        self.colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'black', 'pink', 'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10', 'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19', 'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26']

        # Create a tk variable which will hold the value of the selcted color
        self.selected_color = tk.StringVar()
        self.selected_color.set(self.colors[0])

        # Create radio buttons (list comprehension)
        self.radio_options = [tk.Radiobutton(self, text=color,
                                             value=color,
                                             variable=self.selected_color,
                                             command=self.change_color,
                              )
                              for color in self.colors]

        self.place_widgets()

    def place_widgets(self):
        for ro in self.radio_options:
            ro.pack(side=tk.TOP, anchor='w', padx=(5, 10), pady=5)

    def change_color(self):
        colour = self.selected_color.get()
        self.config(bg=colour)
        self.master.config(bg=colour)
        self.master.clicker_frame.config(bg=colour)

if __name__ == '__main__':
    app = ClickApp()
    app.mainloop()