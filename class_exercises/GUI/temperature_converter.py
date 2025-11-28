import tkinter as tk
from tkinter import ttk
import json
from temperature import Temperature

#MainFrame is a subclass of tk.Frame
class MainFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__()

        unit_options = ['Kelvin', 'Fahrenheit', 'Celsius']

        self.unit_var = tk.StringVar()
        self.unit_var.set("Celsius")
        self.unit_select = ttk.Combobox(self,
                                           textvariable=self.unit_var,
                                           values=unit_options,
                                           )
        self.other_unit_creation()
        
        self.value_var = tk.StringVar()
        self.value_var.set(0)
        self.edt1 = tk.Entry(self,textvariable=self.value_var)
        self.edt2 = tk.Entry(self)
        self.edt3 = tk.Entry(self)
        
        self.btn = tk.Button(self, text = 'Convert', bg = 'deep sky blue',activebackground="sky blue",command=self.convert)
        
        self.config(bg='light goldenrod')
        
        self.place_widget()
        
        parent.bind('<<ComboboxSelected>>',lambda event:self.other_unit_creation())
    
    def convert(self):
        unit_input = self.unit_var.get()
        value_input = self.value_var.get()
        temp = Temperature(int(value_input))
        if unit_input == 'Celsius':
            return (temp.fahrenheit,temp.kelvin)
        elif unit_input == 'Fahrenheit':
            return (temp.celsius,temp.kelvin)
        elif unit_input == 'Kelvin':
            return (temp.celsius,temp.fahrenheit) 
        
    
    def other_unit_creation(self):
        self.other_units = [tk.Label(self, text=unit,
                                     )
                            for unit in self.decide_other_units()]

        settings = {'padx': 10, 'pady': 10, 'sticky': 'snew'}
        count = 0
        for cb in self.other_units:
            count += 1
            cb.grid(row=0, column=count, **settings)

    def place_widget(self):
        settings = {'padx':10, 'pady':10, 'sticky':'nswe'}
        # .pack() puts the stuff as close to the top of the screen as possible
        self.unit_select.grid(row=0,column=0, **settings)
        self.edt1.grid(row=1,column=0, **settings)
        self.edt2.grid(row=1,column=1, **settings)
        self.edt3.grid(row=1,column=2, **settings)
        
        self.btn.grid(row=2,column=0, padx =10, pady=10,sticky='w')

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
    root.geometry("450x130+100+100")
    root.title('Temperature Converter')
    main_frame = MainFrame(root)
    main_frame.pack(fill=tk.BOTH,expand=True,)
    # .mainloop() ensures all structures remain after their line has finished
    root.mainloop()
