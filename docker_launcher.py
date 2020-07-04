from tkinter import *
from dockerfile_generator import *
from functools import partial

# class gui():

#     def __init__(self):    

#         self.master = Tk()
#         self.master.geometry("300x500")
#         self.master.title("Weather App")

#         Label(self.master, text="Your City (e.g Cologne):").grid(row=0, pady=(100,0), padx=(20,0))

#         self.Input_Window = Entry(self.master)

#         self.Input_Window.grid(row=1, column=0, padx=(20,0))

#         Button(self.master, text='Enter', command=self.get_city).grid(row=2, column=0, padx=(20,0), pady=(10,0))

#         self.Output_Window = Text(self.master, height=9, width=30)
#         self.Output_Window.grid(row=3, column=0, pady=(30,0), padx=(20,0))

#         self.Output_Window.insert(END, "")

#         self.master.mainloop()


def empty():
    return

docker_templates = ["Docker-Ubuntu","Docker-Python","Docker-MySQL", "Docker-HTTPD", "Docker-django"]

root = Tk()
root.title("Docker Launcher")
#root.geometry("400x400")

mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 40, padx = 40)

tkvar = StringVar(root)
tkvar.set("Docker-Ubuntu")

Label(mainframe, text="Choose A Docker Template").grid(row = 0, column = 0)
docker_menu = OptionMenu(mainframe, tkvar, *docker_templates)
docker_menu.grid(row=1, column=0)

Label(mainframe, text="Enter Docker Flags").grid(row = 2, column = 0)
docker_flags_input = Entry(mainframe)
docker_flags_input.grid(row=3, column=0)

Label(mainframe, text="Enter Additional Commands").grid(row = 4, column = 0)
additional_commands_input = Entry(mainframe)
additional_commands_input.grid(row=5, column=0)

Button(mainframe, text='Start', command=partial(create_dockerfile, tkvar.get(), docker_flags_input.get(), additional_commands_input.get())).grid(row=6, column=0)
Button(mainframe, text='Save Template', command=empty()).grid(row=6, column=1)





root.mainloop()

#tkvar.get(),docker_flags_input.get(),additional_commands_input.get()