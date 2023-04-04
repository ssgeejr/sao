import os


class MysteryMachine:
    def __init__(self):
        # Get the path to the .openai directory in the user's home directory
        home_directory = os.path.expanduser('~')
        file_path = os.path.join(home_directory, '.openai', 'openapi.pk')
        with open(file_path, 'r') as f:
            contents = f.read()
        for line in contents.split('\n'):
            key, value = line.split('=')
            if key == 'openai_key':
                self.openai_key = value.strip()
            if key == 'openai_orgid':
                self.openai_orgid = value.strip()

    def get_api_key(self):
        return self.openai_key

    def get_organization(self):
        return self.openai_orgid