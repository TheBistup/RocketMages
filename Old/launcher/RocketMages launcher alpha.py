print("[!]Importing...")

import time
import random
import pygame
import sys
from pygame.locals import *
import tkinter
import tkinter.messagebox as msg
from tkinter import ttk
from tkinter import *
import tkinter as tk
import datetime
import os
from PIL import Image, ImageTk

print("[!]Loading game data...")
HUGE = ("Helvetica",46)
BIG = ("Helvetica",16)
Medium = ("Helvetica",12)
small = ("Helvetica",10)

open_program = 0
this_frame = False
print("[!]Finalizing...")

try:
    with open("screensettings","r") as settings:
        settings_string_screen = str(settings.read())
        if settings_string_screen > 0:
            screen_dimensions = int(settings_string_screen)
except:
    screen_dimensions = (1920,1080)


class RocketMages_Setup(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self,"RocketMages Launcher")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames  = {}

        for F in (Launcher, Welcome, Sign_in, News, Future_patches):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0,column=0, sticky="nsew")

        self.show_frame(Launcher)
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


                        
class Launcher(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label_1 = Label(self, text="Rocket Mages Launcher", font=HUGE)
        button_1 = Button(self, text="Proceed", font=Medium, command=lambda: controller.show_frame(Welcome))
        label_2 = Label(self, text="--->", font=small)

        label_1.pack()
        button_1.pack()
        label_2.pack()
class Welcome(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        label_1 = Label(self, text="Welcome", font=HUGE)
        button_1 = Button(self, text="Sign in", command=lambda: controller.show_frame(Sign_in))
        button_2 = Button(self, text="News",command=lambda: controller.show_frame(News))
        button_3 = Button(self, text="Future updates",command=lambda: controller.show_frame(Future_patches))

        label_1.pack()
        button_1.pack()
        button_2.pack()
        button_3.pack()
class Sign_in(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        self.label_1 = Label(self, text="Sign in", font=small)
        entry_1 = Entry(self)
        self.label_2 = Label(self, text="Password", font=small)
        self.entry_2 = Entry(self, show="*")

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)

        self.login_button = Button(self, text="Login", command=Login())

        
        self.login_button.grid(row=2,column=2)
        global entry_1                           

def Login():
    print("[$]Button clicked")
    user_name = str(entry_1.get())
    with open("username.txt","w") as file:
        file.write(user_name)
    this_frame = True
    open_program = 1
    global open_program
    open_main_program()
    
def open_main_program():
    if open_program == 1:
        os.chdir("..\\game\\")
        os.system("start RM-Alpha-1.0.py")
    else:
        print("[$]Cannot open program {RML Error 2}(check error file)")
class News(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        self.label_1 = Label(self, text="Update News and more!", fg="blue", font=BIG)
        self.label_2 = Label(self, text="----------------------------",fg="blue", font=BIG)
        self.label_3 = Label(self, text="---> Version 1.0 released to git hub!\n      ---> Version 1.1 release date revealed!\n                                         ---> Version 1.1 is going to be released to github on the 18th\n\n\n                         ---> Please keep up wih our latest developments! ", font=Medium)
        self.button_1 = Button(self, text="<-- go back", command=lambda: controller.show_frame(Welcome))

        self.label_1.pack()
        self.label_2.pack()
        self.label_3.pack()
        self.button_1.pack()


class Future_patches(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        open_program = 0

        self.label_1 = Label(self, text="Future Changes",fg="green", font=HUGE)
        self.label_2= Label(self, text="In future we hope to add multiplayer and many other amazing functions! keep up with the news by visiting the news page.", font=small)
        self.button_1 = Button(self, text="<-- go back", command= lambda: controller.show_frame(Welcome))
        
        self.label_1.pack()
        self.label_2.pack()
        self.button_1.pack()
    
application = RocketMages_Setup()
application.geometry("1920x1080")
application.mainloop()
print(int(open_program))
    

