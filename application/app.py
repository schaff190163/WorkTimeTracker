import tkinter as tk
from tkinter import ttk
from database_manager import Database_Manager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

engine = create_engine('sqlite:///C:\\Users\\Simon\\OneDrive\\Dokumente\\4AHIT\\SEW INSY\\WorkTimeTracker\\application\\app_db.sql')
Session = sessionmaker(bind=engine)
session = Session()
now = datetime.datetime.now()


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
        mainlabel.grid(row=0, column=0, padx=(0, 0), pady=(10, 0))

        all_users = Database_Manager.get_all_users(session)
        users_list = [user.userName for user in all_users]
        for i, button_name in enumerate(users_list):
            button = ttk.Button(self, text=button_name, width=20,
                                command=lambda:
                                controller.show_frame(Options))
            button.grid(row=i+1, column=1, padx=(0, 100), pady=(10, 10))


class Options(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg='green')
        self.config(width=700, height=450)

        actions_button = ttk.Button(self, text="Actions",
                                    command=lambda:
                                    controller.show_frame(Actions))
        stats_button = ttk.Button(self, text="Statistics",
                                  command=lambda:
                                  controller.show_frame(Statistics))
        back_button = ttk.Button(self, text="Back",
                                 command=lambda:
                                 controller.show_frame(UserSelect))

        actions_button.grid(row=1, column=0, padx=(100, 100), pady=(10, 70))
        stats_button.grid(row=1, column=2, padx=(100, 100), pady=(10, 70))
        back_button.grid(row=0, column=0, padx=(100, 100), pady=(5, 100))


class Actions(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg='yellow')
        self.config(width=700, height=450)

        coming_button = ttk.Button(self, text="Coming",
                                   command=lambda: Database_Manager.create_time
                                   (session, user_id=1, start_value=now, stop_value=None))
        leaving_button = ttk.Button(self, text="Leaving",
                                    command=lambda: Database_Manager.update_time
                                    (session, time_id=1, user_id=1, start_value=now, stop_value=now))
        back_button = ttk.Button(self, text="Back",
                                 command=lambda:
                                 controller.show_frame(Options))

        coming_button.grid(row=1, column=0, padx=(100, 100), pady=(10, 80))
        leaving_button.grid(row=1, column=2, padx=(100, 100), pady=(10, 80))
        back_button.grid(row=0, column=0, padx=(100, 100), pady=(10, 80))


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
