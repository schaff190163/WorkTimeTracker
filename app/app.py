import tkinter as tk


class UserSelect(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_ui()

    def init_ui(self):
        self.button = tk.Button(self, text="Go to Page 2", command=self.go_to_options)
        self.button.pack()

    def go_to_options(self):
        self.pack_forget()
        Options(self.master)


class Options(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_ui()

    def init_ui(self):
        self.button1 = tk.Button(self, text="Button 1")
        self.button1.pack(fill=tk.BOTH, expand=True)
        self.button2 = tk.Button(self, text="Button 2")
        self.button2.pack(fill=tk.BOTH, expand=True)


root = tk.Tk()
root.geometry("700x500")
UserSelect(root).pack()
root.mainloop()
