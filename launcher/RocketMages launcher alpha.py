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


print("[!]Loading game data...")
main = Tk()
BIG = ("Helvetica",12)
Medium = ("Helvetica",10)
small = ("Helvetica",8)
print("[!]Finalizing...")
main.wm_title("RocketMages launcher")

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
        label_1 = Label(self, text="Rocket Mages Launcher", font=BIG)
        button_1 = Button(self, text="Proceed", font=Medium, command=lambda: controller.show_frame(Welcome))
        label_2 = Label(self, text="--->", font=small)

        label_1.pack()
        button_1.pack()
        label_2.pack()
class Welcome(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        label_1 = Label(self, text="Welcome", font=BIG)
        button_1 = Button(self, text="Sign in", command=lambda: controller.show_frame(Sign_in))
        button_2 = Button(self, text="News",command=lambda: controller.show_frame(News))

        label_1.pack()
        button_1.pack()
        button_2.pack()
class Sign_in(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        self.label_1 = Label(self, text="Sign in", font=small)
        self.entry_1 = Entry(self)
        self.label_2 = Label(self, text="Password", font=small)
        self.entry_2 = Entry(self, show="*")

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)

        self.login_button = Button(self, text="Login", command=open_main_program())


        self.login_button.pack()


def open_main_program():
    os.chdir("..\\game\\")
    os.system("start RM-Alpha-1.0.py")
class News(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        self.label_1 = Label(self, text= "Update News and more!", fg="blue", font=BIG)
        self.label_2 = Label(self, text="--------------------------",fg="blue", font=BIG)
        self.label_3 = Label(self, text="---> Version 1.0 released to git hub!", font=Medium)
        self.button_1 = Button(self, text="<-- go back", command=lambda: controller.show_frame(Welcome))

        self.pack()


class Future_patches(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        self.label_1 = Label(self, text="Future Changes",fg="green", font=BIG)
        self.label_2= Label(self, text="In future we hope to add multiplayer and many other amazing functions! keep up with the news by visiting the news page.", font=small)
        self.button_1 = Button(self, text="<-- go back", command= lambda: controller.show_frame(Welcome) )
    
application = RocketMages_Setup()
application.geometry("1920x1080")
application.mainloop()
    

