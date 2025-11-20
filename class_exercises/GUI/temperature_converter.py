import tkinter as tk
from tkinter import ttk
import json

#MainFrame is a subclass of tk.Frame
class MainFrame(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        unit_options = ['Kelvin', 'Fahrenheit', 'Celsius']

        self.unit_var = tk.StringVar()
        self.unit_var.set("Celsius")
        self.unit_select = ttk.Combobox(self,
                                           textvariable=self.unit_var,
                                           values=unit_options,
                                           )

        self.other_units = [tk.Text(self, text=unit,
                              )
                              for unit in self.decide_other_units()]

        self.edt = tk.Entry(self)

        self.place_widget()

    def place_widget(self):
        settings = {'padx':10, 'pady':10, 'sticky':'w'}
        # .pack() puts the stuff as close to the top of the screen as possible
        self.unit_select.grid(row=0,column=0, **settings)
        self.edt.grid(row=1,column=0, **settings)

        for

    def decide_other_units (self):
        input = self.unit_var.get()
        if input == 'Celsius':
            return ('Fahrenheit', 'Kelvin')
        elif input == 'Fahrenheit':
            return ('Celsius', 'Kelvin')
        elif input == 'Kelvin':
            return ('Celsius', 'Fahrenheit')

if __name__ == '__main__':
    # root sets up a blank page to act as a background
    root = tk.Tk()
    root.geometry("500x500+100+100")
    root.title('Temperature Converter')
    main_frame = MainFrame(root)
    main_frame.pack(fill=tk.BOTH,expand=True)
    # .mainloop() ensures all structures remain after their line has finished
    root.mainloop()