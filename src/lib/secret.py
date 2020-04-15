import json
import os

class SecretReader :

    def __init__(self, secretDirectory='./secrets', secretExtension='.secret') :
        self.secretDirectory = secretDirectory
        self.secretExtension = secretExtension

    def read(self, secretName) :
        try :
            secretFile = open(os.path.join(self.secretDirectory, secretName + self.secretExtension), 'r')
            return json.loads(secretFile.read())
        except FileNotFoundError :
            return None