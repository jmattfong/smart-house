from lib.account.account import Account

class RingAccount(Account) :

    def __init__(self, secret_reader):
        super().__init__('ring', secret_reader)

    def connect_with_credentials(self, credentials) :
        pass

    def disconnect_and_forget(self) :
        pass
