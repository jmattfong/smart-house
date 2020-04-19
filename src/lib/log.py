import sys
import datetime

def logger(cls):
    cls.log = Logger(cls.__name__)
    return cls

class Logger :

    def __init__(self, name) :
        self.name = name

    def debug(self, message) :
        print(f'{datetime.datetime.now()}, DEBUG, {self.name}: {message}', file=sys.stderr)

    def info(self, message) :
        print(f'{datetime.datetime.now()}, INFO,  {self.name}: {message}', file=sys.stderr)

    def warn(self, message) :
        print(f'{datetime.datetime.now()}, WARN,  {self.name}: {message}', file=sys.stderr)

    def error(self, message) :
        print(f'{datetime.datetime.now()}, ERROR, {self.name}: {message}', file=sys.stderr)
