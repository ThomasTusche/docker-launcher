import docker
from io import BytesIO
from tkinter import messagebox
class DockerFileCreator:

    def __init__(self):
        print("hallo")

    @classmethod
    def create_dockerfile(cls):
        return
    
    @classmethod
    def build_image(cls, file): 

        try:
            dockerfile = open(file, mode='rb')

            client = docker.from_env()

            build,log = client.images.build(fileobj = dockerfile, tag=file, rm=True)
        
            for line in log:
                print(line)

            messagebox.showinfo(f"Success", "Successfully build Docker image.")
        except:
            messagebox.showerror("error", "Couldn't find the image.\nPlease use a different template or build the image first.")
            

    @classmethod
    def run_container(cls, myimage, mycommand=None, myentrypoint=None, myhostname=None, port=None, deletion=False, mountfolder=None, mountpath=None, mountpermission=None):
        client = docker.from_env()

        if port:
            port = {port.split(":")[0]:port.split(":")[1]}

        if deletion:
            deletion = True
        elif not deletion:
            deletion = False

        if mountfolder:
            if not mountpath:
                mountpath = '/mnt/vol1'
            if mountpermission == 1:
                mountpermission = "rw"
            elif mountpermission == 0:
                mountpermission = "ro"
            mount = {mountfolder:{"bind":mountpath,"mode":mountpermission}}
        elif not mountfolder:
            mount = None
        try:
            client.images.get(myimage)

            try:
                client.containers.run(image=myimage,command=mycommand,ports=port,hostname=myhostname,auto_remove=deletion,volumes=mount,detach=True)
                messagebox.showinfo(f"Success", "Successfully run container.")
                
            except:
                messagebox.showerror("error", "Problems with running the container.\nPlease review your Dockerfile Template.")           
        except:
            messagebox.showerror("error", "Couldn't find the image.\nPlease use a different template or build the image first.")





    @classmethod
    def save_as(cls):
        print("hello")

#, auto_remove=True