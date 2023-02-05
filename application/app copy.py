import tkinter as tk
from tkinter import ttk


class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.geometry("700x450")
        self.frames = {}

        for F in (UserSelect, Options, Actions, Statistics):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0)

        self.show_frame(UserSelect)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


class UserSelect(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg='red')
        self.config(width=700, height=450)

        mainlabel = ttk.Label(self, text="Select User", font=(
                              'Helvetica bold', 15))
        mainlabel.grid(row=0, column=1, padx=(0, 0), pady=(10, 0))

        button_names = ['Simon', 'John', 'Jane', 'Alex']
        for i, button_name in enumerate(button_names):
            button = ttk.Button(self, text="User " + str(i+1), width=20,
                                command=lambda:
                                controller.show_frame(Options))
            button.grid(row=i+1, column=100, padx=(0, 100), pady=(10, 10))


class Options(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg='green')
        self.config(width=700, height=450)

        mainlabel = ttk.Label(self, text="What do you want to do?", font=(
                              'Helvetica bold', 15))
        back_button = ttk.Button(self, text="Back",
                                 command=lambda:
                                 controller.show_frame(UserSelect))

        mainlabel.grid(row=0, column=1, padx=(0, 0), pady=(80, 10))
        back_button.grid(row=5, column=1, padx=(100, 100), pady=(10, 80))


class Actions(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg='yellow')
        self.config(width=700, height=450)

        mainlabel = ttk.Label(self, text="Are you entering or leaving?", font=(
                              'Helvetica bold', 15))
        back_button = ttk.Button(self, text="Back",
                                 command=lambda:
                                 controller.show_frame(Options))

        mainlabel.grid(row=0, column=1, padx=(0, 0), pady=(80, 10))
        back_button.grid(row=1, column=1, padx=(100, 100), pady=(10, 80))


class Statistics(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg='blue')
        self.config(width=700, height=450)

        mainlabel = ttk.Label(self, text="Statistics", font=(
                              'Helvetica bold', 15))

        mainlabel.grid(row=0, column=1, padx=(0, 0), pady=(80, 10))


app = tkinterApp()
app.mainloop()
