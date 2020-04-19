import sys
import traceback

from abc import ABCMeta, abstractmethod
from lib.util import auto_str
from lib.log import logger

@logger
@auto_str
class Account(metaclass=ABCMeta) :

    def __init__(self, account_name, secret_reader) :
        self.account_name = account_name
        self.secret_reader = secret_reader
        self.is_connected = False

    def connect(self) :
        credentials = self.secret_reader.read(self.account_name)
        if credentials == None :
            self.log.warn(f"No credentials found for account type '{self.account_name}'.")
        else :
            self.log.info(f"Account '{self.account_name}' connecting...")
            try :
                self.connect_with_credentials(credentials)
                self.is_connected = True
            except :
                self.log.error(f"Account '{self.account_name}' failed to connect.")
                traceback.print_exc()

    @abstractmethod
    def connect_with_credentials(self, credentials) :
        pass

    def disconnect(self) :
        self.log.info(f"Disconnecting from account '{self.account_name}'")
        self.is_connected = False
        self.disconnect_and_forget()

    @abstractmethod
    def disconnect_and_forget(self) :
        pass
