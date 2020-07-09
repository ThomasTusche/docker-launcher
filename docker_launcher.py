from tkinter import *
from tkinter import filedialog
from functools import partial

# import dockerfile_generator methods
from dockerfile_generator import *

# import info pop up methods
from info_popup import *

#import os to get the absolut path of the py files and list the templates content
from os import path
from os import listdir
from os import name
from os import chdir

#import platform to get the operating system
from platform import system

def mount_file():
    filename = filedialog.askopenfilename()
    select_folder_tkvar.set(filename)
    return

def mount_folder():
    filename = filedialog.askdirectory()
    select_folder_tkvar.set(filename)

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

docker_templates = [f for f in listdir(".")]
docker_templates.append("New Template")

# Creating the Tkinter GUI
root = Tk()
root.title("Docker Launcher")
root.iconphoto(False, PhotoImage(file='../logo.png'))
#root.iconbitmap("tt_logo.bmp")

# creating the mainframe on which everythin is displayed
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 40, padx = 40)

# Display the dropdown menu to choose a docker template
Label(mainframe, text="Choose Template:").grid(row = 1, column = 0)
templates_tkvar = StringVar()
templates_tkvar.set("")
docker_menu = OptionMenu(mainframe, templates_tkvar, *docker_templates, command=get_dockerfile_text)
docker_menu.grid(row=1, column=1)

# The input box for docker command
Label(mainframe, text="Command:").grid(row = 2, column = 0)
docker_command = Entry(mainframe)
docker_command.grid(row=2, column=1)

command_info = Label(mainframe, text="?")
command_info.grid(row = 2, column = 2)
CreateToolTip(command_info, text = "Enter own command, e.g. echo Hello World")

# The input box for a docker entrypoint
Label(mainframe, text="Entrypoint:").grid(row = 3, column = 0)
docker_entrypoint = Entry(mainframe)
docker_entrypoint.grid(row=3, column=1)

entrypoint_info = Label(mainframe, text="?")
entrypoint_info.grid(row = 3, column = 2)
CreateToolTip(entrypoint_info, text = "Enter own entrypoint here, e.g. echo Hello World")

# Input box to enter a container hostname
Label(mainframe, text="Hostname:").grid(row = 4, column = 0)
docker_hostname = Entry(mainframe)
docker_hostname.grid(row=4, column=1)

hostname_info = Label(mainframe, text="?")
hostname_info.grid(row = 4, column = 2)
CreateToolTip(hostname_info, text = "Enter Container's Hostname here")

# Input box for enter docker port to open
Label(mainframe, text="Ports:").grid(row = 5, column = 0)
docker_ports = Entry(mainframe)
docker_ports.grid(row=5, column=1)

docker_info = Label(mainframe, text="?")
docker_info.grid(row = 5, column = 2)
CreateToolTip(docker_info, text = "Enter ports in dict format where keys are the docker ports and values are the host port, e.g 80:8080 ")

# Checkbox to decide whether a container will be removed after closing
Label(mainframe, text="Remove Container after run:").grid(row = 6, column = 0)
yes_tickbox_tkvar = IntVar()
Checkbutton(mainframe, text="Yes", variable=yes_tickbox_tkvar).grid(row = 6, column = 1)

remove_container_info = Label(mainframe, text="?")
remove_container_info.grid(row = 6, column = 2)
CreateToolTip(remove_container_info, text = "If enabled the container will be removed after its run")

# Button to choose the mount folder
Label(mainframe, text="Mount folder:").grid(row = 7, column = 0)
select_folder_tkvar = StringVar()
select_folder_tkvar.set("")
Label(mainframe, textvariable=select_folder_tkvar).grid(row = 7, column = 1)
Button(mainframe, text='Folder', command=mount_folder).grid(row=7, column=2)

mount_info = Label(mainframe, text="?")
mount_info.grid(row = 7, column = 3)
CreateToolTip(mount_info, text = "Choose a folder which will be mounte to tmp/ in the container")

# Chose path within the container to mount the folder 
Label(mainframe, text="Mount Target:").grid(row = 8, column = 0)
docker_path = Entry(mainframe)
docker_path.grid(row=8, column=1)

rw_tickbox_tkvar = IntVar()
Checkbutton(mainframe, text="R/W", variable=rw_tickbox_tkvar).grid(row = 8, column = 2)

path_info = Label(mainframe, text="?")
path_info.grid(row = 8, column = 3)
CreateToolTip(path_info, text = "Choose the location to mount the folder to. Default is '/mnt/vol1'.\nTick R/W for write access. Default is read-only ")

# Textbox to display the Dockerfile content
Label(mainframe, text="Dockerfile:").grid(row = 9, column = 0)
docker_file_content = Text(mainframe)
docker_file_content.grid(row = 9, column = 1)
docker_file_content.insert(END, get_dockerfile_text("Choose Template"))

Button(mainframe, text='Run', command=lambda: DockerFileCreator.run_container(templates_tkvar.get(),docker_command.get(),docker_entrypoint.get(),docker_hostname.get(),docker_ports.get(),yes_tickbox_tkvar.get(),select_folder_tkvar.get(),docker_path.get(),rw_tickbox_tkvar.get())).grid(row=10, column=0)
Button(mainframe, text='Build Image', command=lambda: DockerFileCreator.build_image(templates_tkvar.get())).grid(row=10, column=1)
Button(mainframe, text='Save', command=save).grid(row=10, column=2)
Button(mainframe, text='Save as', command=save_as).grid(row=10, column=3)

root.mainloop()