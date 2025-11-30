import tkinter as tk
from tkinter import ttk
import json
from temperature import Temperature

#MainFrame is a subclass of tk.Frame
class MainFrame(tk.Frame,Temperature):

    def __init__(self, parent):
        super().__init__()
        self.temp = Temperature(celsius=0)

        unit_options = ['kelvin', 'fahrenheit', 'celsius']

        self.unit_var = tk.StringVar()
        self.unit_var.set("celsius")
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

        self.place_edt_boxes()
        
        parent.bind('<<ComboboxSelected>>',lambda event:self.other_unit_creation())

        self.edt1.bind("<KeyRelease>", lambda event: self.convert())

    def convert(self):
        unit_input = self.unit_var.get().lower()

        try:
            value = float(self.value_var.get())
        except ValueError:
            return  'incorrect value entered'

        if unit_input == "celsius":
            self.temp.celsius = value
            out1 = self.temp.fahrenheit
            out2 = self.temp.kelvin
        elif unit_input == "fahrenheit":
            self.temp.fahrenheit = value
            out1 = self.temp.celsius
            out2 = self.temp.kelvin
        elif unit_input == "kelvin":
            self.temp.kelvin = value
            out1 = self.temp.celsius
            out2 = self.temp.fahrenheit

        self.edt2.delete(0, tk.END)
        self.edt3.delete(0, tk.END)
        self.edt2.insert(0, f"{out1:.2f}")
        self.edt3.insert(0, f"{out2:.2f}")
        
    
    def other_unit_creation(self):
        self.other_units = [tk.Label(self, text=unit,
                                     )
                            for unit in self.decide_other_units()]

        settings = {'padx': 10, 'pady': 10, 'sticky': 'snew'}
        count = 0
        for cb in self.other_units:
            count += 1
            cb.grid(row=0, column=count, **settings)

    def place_edt_boxes(self):
        settings = {'padx': 10, 'pady': 10, 'sticky': 'nswe'}
        self.edt2.grid(row=1, column=1, **settings)
        self.edt3.grid(row=1, column=2, **settings)

    def place_widget(self):
        settings = {'padx':10, 'pady':10, 'sticky':'nswe'}
        # .pack() puts the stuff as close to the top of the screen as possible
        self.unit_select.grid(row=0,column=0, **settings)
        self.edt1.grid(row=1,column=0, **settings)

        self.btn.grid(row=2,column=0, padx =10, pady=10,sticky='w')

    def decide_other_units (self):
        input = self.unit_var.get()
        if input == 'celsius':
            return ('fahrenheit', 'kelvin')
        elif input == 'fahrenheit':
            return ('celsius', 'kelvin')
        elif input == 'kelvin':
            return ('celsius', 'fahrenheit')

if __name__ == '__main__':
    # root sets up a blank page to act as a background
    root = tk.Tk()
    root.geometry("450x130+100+100")
    root.title('Temperature Converter')
    main_frame = MainFrame(root)
    main_frame.pack(fill=tk.BOTH,expand=True,)
    # .mainloop() ensures all structures remain after their line has finished
    root.mainloop()
