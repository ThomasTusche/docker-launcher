from tkinter import *
from tkinter import filedialog
from dockerfile_generator import *
from functools import partial

#import os to get the absolut path of the py files and list the templates content
from os import path
from os import listdir
from os import name
from os import chdir

#import platform to get the operating system
from platform import system

# functions for the tkinter interface
def mount_file():
    filename = filedialog.askopenfilename()
    select_folder_tkvar.set(f"Script to mount: {filename}")
    return

def mount_folder():
    filename = filedialog.askdirectory()
    select_folder_tkvar.set(f"Folder to mount: {filename}")

def save():
    filename = templates_tkvar.get()
    with open(filename, "w") as file:
        file.write(docker_file_content.get("1.0",END))    
    
def save_as():
    filename = filedialog.asksaveasfile(mode="w")
    if filename is None:
        return
    text2save = docker_file_content.get("1.0",END)
    filename.write(text2save)
    filename.close()
    
def open_file():
    file = filedialog.askopenfilename()
    select_folder_tkvar.set(file)

def get_dockerfile_text(dockerfile):
    filename = dockerfile
    if filename == "Choose Template":
        return ""
    elif filename == "New Template":
        docker_file_content.delete("1.0", END)
        return
    with open(filename, mode='r') as file:
        data = file.read()
        docker_file_content.delete("1.0", END)
        docker_file_content.insert("1.0", data)        
    return data



# Find operating system for setting the file path
operating_system = system()

# Change working directory to the python folder that I can use relatives paths
if operating_system == "Windows":
    template_path = f"{path.dirname(path.abspath(__file__))}\\templates"
    chdir(template_path)
elif operating_system == "Linux":
    #template_path = f"{path.dirname(path.abspath(__file__))}/templates"
    chdir(path.dirname(path.abspath(__file__)))
elif operating_system == "Mac":
    #template_path = f"{path.dirname(path.abspath(__file__))}\\templates"
    chdir(path.dirname(path.abspath(__file__)))

# list all template files to display in tkinter OptionMenu
docker_templates = [f for f in listdir(".")]
docker_templates.append("New Template")

# Creating the Tkinter GUI
root = Tk()
root.title("Docker Launcher")

mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 40, padx = 40)

templates_tkvar = StringVar(root)
templates_tkvar.set("Choose Template")
docker_menu = OptionMenu(mainframe, templates_tkvar, *docker_templates, command=get_dockerfile_text)
docker_menu.grid(row=1, column=0)

Label(mainframe, text="Enter Docker Flags").grid(row = 2, column = 0)
docker_flags_input = Entry(mainframe)
docker_flags_input.grid(row=3, column=0)

select_folder_tkvar = StringVar(root)
select_folder_tkvar.set("Select Script or Folder to mount: ")
Label(mainframe, textvariable=select_folder_tkvar).grid(row = 4, column = 0)
Button(mainframe, text='File', command=mount_file).grid(row=4, column=1)
Button(mainframe, text='Folder', command=mount_folder).grid(row=4, column=2)
#Label(mainframe, textvariable=select_folder_tkvar).grid(row = 5, column = 0)

Label(mainframe, text="Dockerfile").grid(row = 6, column = 0)
docker_file_content=Text(mainframe)
docker_file_content.grid(row = 7, column = 0)
docker_file_content.insert(END, get_dockerfile_text("Choose Template"))

Button(mainframe, text='Run', command=lambda: DockerFileCreator.run_container(templates_tkvar.get())).grid(row=8, column=0)
Button(mainframe, text='Build Image', command=lambda: DockerFileCreator.build_image(templates_tkvar.get())).grid(row=8, column=1)
Button(mainframe, text='Save', command=save).grid(row=8, column=2)
Button(mainframe, text='Save as', command=save_as).grid(row=8, column=3)
#Button(mainframe, text='Run', command=lambda: DockerFileCreator.run_container(f"{path.dirname(path.abspath(__file__))}\\templates\\{tkvar.get()}").grid(row=6, column=0)
# Button(mainframe, text='Display Dockerfile', command=DockerFileCreator.test).grid(row=6, column=1)
# Button(mainframe, text='Refresh', command=DockerFileCreator.test).grid(row=6, column=2)
# Button(mainframe, text='Upload File', command=DockerFileCreator.test).grid(row=6, column=3)
# Button(mainframe, text='Save Template', command=DockerFileCreator.test).grid(row=6, column=4)

root.mainloop()