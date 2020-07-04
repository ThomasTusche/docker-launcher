import docker
class DockerFileCreator:

    def __init__(self):
        self.run_container()

    @classmethod
    def create_dockerfile(cls):
        return
    
    @classmethod
    def run_container(cls):
        image = "pythontest"
        client = docker.from_env()
        client.containers.run(image, auto_remove=True)

    def test(self):
        return

#DockerFileCreator.run_container()