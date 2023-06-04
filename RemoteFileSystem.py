from os import environ
from github import Github

class RemoteFileSystem:
    
    def __init__(self):
        self.g = Github(environ.get('GITHUB_TOKEN'))
        self.repository = self.g.get_user().get_repo('file_system_experiment')
        

    def read_file(self, filename):
        f = self.repository.get_contents(filename)
        file_decoded = f.decoded_content.decode()
        print("read_file")
        return file_decoded

    def update_file(self, filename, content):
        # create with commit message
        #print(content)
        print("update_file")
        contents = self.repository.get_contents(filename, ref="main")
        self.repository.update_file(contents.path, "Update file " + filename, content, contents.sha, branch="main")
