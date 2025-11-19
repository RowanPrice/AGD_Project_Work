import tkinter as tk
from tkinter import ttk

class MainFrame(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.txt1 = tk.Label(self, text="Registration Form", font=("Arial", 20))
        self.txt1.pack(side=tk.TOP)
        self.txt2 = tk.Label(self, text="Full Name",font=("Arial", 12))
        self.txt3 = tk.Label(self, text="Email",font=("Arial", 12))
        self.txt4 = tk.Label(self, text="Gender",font=("Arial", 12))
        self.txt5 = tk.Label(self, text="Country",font=("Arial", 12))
        self.txt6 = tk.Label(self, text="Programming",font=("Arial", 12))

        self.edt1= tk.Entry(self)
        self.edt2= tk.Entry(self)

        self.ro1 = tk.Radiobutton(self, text="Male", value=1)
        self.ro2 = tk.Radiobutton(self, text="Female", value=2)

        self.cb = ttk.Combobox(self, values=['United States', 'Canada', 'United Kingdom', 'Australia', 'Germany', 'France', 'India', 'China', 'Japan', 'Brazil'])

        self.check1 = ttk.Checkbutton(self, text="Java", variable=0)
        self.check2 = ttk.Checkbutton(self, text="Python", variable=1)

        self.btn = tk.Button(self, text="Submit")

        self.place_widget()



    def place_widget(self):
        settings = {'padx': 10, 'pady': 10, 'sticky': 'w'}
        self.txt1.grid(row=0, column=0, **settings)
        self.txt2.grid(row=1, column=0, **settings)
        self.txt3.grid(row=2, column=0, **settings)
        self.txt4.grid(row=3, column=0, **settings)
        self.txt5.grid(row=4, column=0, **settings)
        self.txt6.grid(row=5, column=0, **settings)

        self.edt1.grid(row=1, column=1, **settings)
        self.edt2.grid(row=2, column=1, **settings)

        self.ro1.grid(row=3, column=1, **settings)
        self.ro2.grid(row=3, column=2, **settings)

        self.cb.grid(row=4, column=1, **settings)

        self.check1.grid(row=5, column=1, **settings)
        self.check2.grid(row=5, column=2, **settings)

        self.btn.grid(row=6, column=0, **settings)





if __name__ == '__main__':
        root = tk.Tk()
        root.geometry("500x350+100+100")
        root.title("Registration Form")
        main_frame = MainFrame(root)
        main_frame.pack(fill=tk.BOTH, expand=True)
        root.mainloop()