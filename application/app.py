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

    current_user_id = 0

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

    @staticmethod
    def getUserID():
        return tkinterApp.current_user_id

    @staticmethod
    def setUserID(user_ID):
        tkinterApp.current_user_id = user_ID


class UserSelect(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=700, height=450)

        mainlabel = ttk.Label(self, text="Select User", font=(
                              'Helvetica bold', 15))
        mainlabel.grid(row=0, column=0, padx=(0, 0), pady=(10, 10))

        users = Database_Manager.get_all_users(session)
        for i, user in enumerate(users):
            button = ttk.Button(self, text=user.userName, width=50,
                                command=UserSelect.generate_lambda(user.userID, controller))

            button.grid(row=i+1, column=0, padx=(150, 150), pady=(10, 10))

    def generate_lambda(user_id, controller):
        return lambda: UserSelect.setID(user_id, controller)

    def setID(user_id, controller):
        tkinterApp.setUserID(user_id)

        controller.show_frame(Options)
        print(user_id)


class Options(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=700, height=450)

        mainlabel = ttk.Label(self, text="Options", font=(
                              'Helvetica bold', 15))
        actions_button = ttk.Button(self, text="Actions",
                                    command=lambda:
                                    controller.show_frame(Actions),
                                    width=20)
        stats_button = ttk.Button(self, text="Statistics",
                                  command=lambda:
                                  controller.show_frame(Statistics),
                                  width=20)
        back_button = ttk.Button(self, text="Back",
                                 command=lambda:
                                 controller.show_frame(UserSelect))

        mainlabel.grid(row=0, column=1, padx=(10, 10), pady=(10, 50))
        actions_button.grid(row=1, column=0, padx=(75, 75), pady=(25, 85))
        stats_button.grid(row=1, column=2, padx=(75, 75), pady=(25, 85))
        back_button.grid(row=0, column=0, padx=(10, 50), pady=(10, 50))


class Actions(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=700, height=450)
        tk.IntVar()

        self.selected_user = 0
        mainlabel = ttk.Label(self, text="Are you entering or leaving?", font=(
                              'Helvetica bold', 15))
        coming_button = ttk.Button(self, text="Entering",
                                   command=lambda: [
                                    Database_Manager.create_time(session, user_id=tkinterApp.getUserID(), start_value=now, stop_value=None),
                                    controller.show_frame(Options)
                                    ], width=20)
        leaving_button = ttk.Button(self, text="Leaving",
                                    command=lambda: [
                                    Database_Manager.update_time(session, user_id=tkinterApp.getUserID(), stop_value=now),
                                    controller.show_frame(Options)
                                    ], width=20)
        back_button = ttk.Button(self, text="Back",
                                 command=lambda:
                                 controller.show_frame(Options))

        mainlabel.grid(row=0, column=1, padx=(10, 10), pady=(10, 50))
        coming_button.grid(row=1, column=0, padx=(75, 75), pady=(25, 85))
        leaving_button.grid(row=1, column=2, padx=(75, 75), pady=(25, 85))
        back_button.grid(row=0, column=0, padx=(10, 50), pady=(10, 50))


class Statistics(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=700, height=450)

        user_id = tkinterApp.getUserID()
        print(user_id)

        mainlabel = ttk.Label(self, text="Statistics", font=(
                              'Helvetica bold', 15))
        yearlabel = ttk.Label(self, text="This Year:")
        monthlabel = ttk.Label(self, text="This Month:")
        weeklabel = ttk.Label(self, text="This Week:")

        yearval = ttk.Label(self, text="%.1f h" % Database_Manager.get_sum_of_year(session, user_id=tkinterApp.getUserID()))
        monthval = ttk.Label(self, text="%.1f h" % Database_Manager.get_sum_of_month(session, user_id=tkinterApp.getUserID()))
        weekval = ttk.Label(self, text="%.1f h" % Database_Manager.get_sum_of_week(session, user_id=tkinterApp.getUserID()))
        back_button = ttk.Button(self, text="Back",
                                 command=lambda:
                                 controller.show_frame(Options))

        mainlabel.grid(row=0, column=1, padx=(10, 10), pady=(10, 50))
        yearlabel.grid(row=1, column=0, padx=(30, 30), pady=(10, 10))
        monthlabel.grid(row=2, column=0, padx=(30, 30), pady=(10, 10))
        weeklabel.grid(row=3, column=0, padx=(30, 30), pady=(10, 10))
        yearval.grid(row=1, column=1, padx=(300, 50), pady=(10, 10))
        monthval.grid(row=2, column=1, padx=(300, 50), pady=(10, 10))
        weekval.grid(row=3, column=1, padx=(300, 50), pady=(10, 10))
        back_button.grid(row=0, column=0, padx=(10, 10), pady=(10, 50))


app = tkinterApp()
app.mainloop()
