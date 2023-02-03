import tkinter as tk
from tkinter import ttk


LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Shopping_List, Create_List, Older_Lists):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0)

        self.show_frame(Shopping_List)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Shopping_List(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        mainlabel = ttk.Label(self, text="Shopping List", font=(
                              'Helvetica bold', 15))
        button1 = ttk.Button(self, text="Create List",
                             command=lambda:
                             controller.show_frame(Create_List))
        button2 = ttk.Button(self, text="Older Lists",
                             command=lambda:
                             controller.show_frame(Older_Lists))

        mainlabel.grid(row=0, column=1, padx=(0, 0), pady=(80, 10))
        button1.grid(row=1, column=1, padx=(100, 100), pady=(10, 10))
        button2.grid(row=2, column=1, padx=(100, 100), pady=(10, 80))


class Create_List(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        mainlabel = ttk.Label(self, text="Create List", font=(
                              'Helvetica bold', 15))
        label1 = ttk.Label(self, text="List Name")
        entry1 = ttk.Entry(self, width=10)
        label2 = ttk.Label(self, text="List Date")
        entry2 = ttk.Entry(self, width=10)
        back_button = ttk.Button(self, text="Back",
                                 command=lambda:
                                 controller.show_frame(Shopping_List))

        mainlabel.grid(row=0, column=1, padx=(0, 0), pady=(80, 10))
        label1.grid(row=1, column=1, padx=(100, 100), pady=(10, 0))
        entry1.grid(row=2, column=1, padx=(0, 0), pady=(10, 10))
        label2.grid(row=3, column=1, padx=(100, 100), pady=(10, 0))
        entry2.grid(row=4, column=1, padx=(0, 0), pady=(10, 10))
        back_button.grid(row=5, column=1, padx=(100, 100), pady=(10, 80))


class Older_Lists(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        mainlabel = ttk.Label(self, text="Older Lists", font=(
                              'Helvetica bold', 15))
        back_button = ttk.Button(self, text="Back",
                                 command=lambda:
                                 controller.show_frame(Shopping_List))

        mainlabel.grid(row=0, column=1, padx=(0, 0), pady=(80, 10))
        back_button.grid(row=1, column=1, padx=(100, 100), pady=(10, 80))


app = tkinterApp()
app.mainloop()
