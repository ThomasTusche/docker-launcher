import docker
from io import BytesIO
class DockerFileCreator:

    def __init__(self):
        print("hallo")

    @classmethod
    def create_dockerfile(cls):
        return
    
    @classmethod
    def build_image(cls, file): 

        dockerfile = open(file, mode='rb')

        client = docker.from_env()

        build,log = client.images.build(fileobj = dockerfile, tag=file, rm=True)
        
        print(build)
        for line in log:
            print(line)

    @classmethod
    def run_container(cls, image):
        client = docker.from_env()
        client.containers.run(image)

    @classmethod
    def save_as(cls):
        print("hello")

#, auto_remove=True