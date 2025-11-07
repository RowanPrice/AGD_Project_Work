import tkinter as tk

#MainFrame is a subclass of tk.Frame
class MainFrame(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.txt = tk.Label(self,text="My tkinter app",bg="black",fg="red",)
        self.btn = tk.Button(self,text="Do not press",bg="black",fg="red",activebackground="red",activeforeground="black",)
        self.edt = tk.Entry(self)
        self.sld = tk.Scale(self,from_=0,to=100,orient=tk.VERTICAL,bg="black",fg="red")

        self.config(bg="black")


        self.place_widget()

    def place_widget(self):
        # .pack() puts the stuff as close to the top of the screen as possible
        self.txt.grid(row=1,column=1,padx=10,pady=10)
        self.btn.grid(row=1,column=0,padx=10,pady=10)
        self.edt.grid(row=0,column=1,padx=10,pady=10)
        self.sld.grid(row=0,column=0,padx=10,pady=10)

if __name__ == '__main__':
    # root sets up a blank page to act as a background
    root = tk.Tk()
    root.title("My tkinter app")
    main_frame = MainFrame(root)
    main_frame.pack(fill=tk.BOTH,expand=True)
    # .mainloop() ensures all structures remain after their line has finished
    root.mainloop()