from tkinter import *
from dockerfile_generator import *
from functools import partial

#import os to get the absolut path of the py files and list the templates content
from os import path
from os import listdir
from os import name

#import platform to get the operating system
from platform import system

# Find operating system for setting the file path
os = system()
# Set path to template folder depending on OS

if os == "Windows":
    template_path = f"{path.dirname(path.abspath(__file__))}\\templates"
elif os == "Linux":
    template_path = f"{path.dirname(path.abspath(__file__))}/templates"
elif os == "Mac":
    template_path = f"{path.dirname(path.abspath(__file__))}\\templates"

#list all template files to display in tkinter OptionMenu
docker_templates = [f for f in listdir(template_path)]

# Creating the Tkinter GUI
root = Tk()
root.title("Docker Launcher")
#root.geometry("400x400")

mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 40, padx = 40)

tkvar = StringVar(root)
tkvar.set(docker_templates[0])

Label(mainframe, text="Choose A Docker Template").grid(row = 0, column = 0)
docker_menu = OptionMenu(mainframe, tkvar, *docker_templates)
docker_menu.grid(row=1, column=0)

Label(mainframe, text="Enter Docker Flags").grid(row = 2, column = 0)
docker_flags_input = Entry(mainframe)
docker_flags_input.grid(row=3, column=0)

Label(mainframe, text="Enter Additional Commands").grid(row = 4, column = 0)
additional_commands_input = Entry(mainframe)
additional_commands_input.grid(row=5, column=0)

Button(mainframe, text='Run', command=DockerFileCreator.run_container).grid(row=6, column=0)
# Button(mainframe, text='Display Dockerfile', command=DockerFileCreator.test).grid(row=6, column=1)
# Button(mainframe, text='Refresh', command=DockerFileCreator.test).grid(row=6, column=2)
# Button(mainframe, text='Upload File', command=DockerFileCreator.test).grid(row=6, column=3)
# Button(mainframe, text='Save Template', command=DockerFileCreator.test).grid(row=6, column=4)

root.mainloop()