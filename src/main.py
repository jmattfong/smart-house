#!/usr/bin/env python3

import sys

from argparse import ArgumentParser
from lib.secret import SecretReader
from lib.account.ring import RingAccount
from lib.log import logger, Logger

def main() :
    MainCLI().run()

@logger
class MainCLI :

    def __init__(self) :
        self.supported_accounts = {}

        self.parser = ArgumentParser(description='Central hub for your smart home')
        self.parser.add_argument(
            '-n', '--home-name',
            help="""The name of your home.
            Must have a matching secret in <secret-directory>/<home-name>.secret that describes the shape of the home.""",
            required=True,
        )
        self.parser.add_argument(
            '-s', '--secret-directory',
            help="""The directory containing your secret files. Passwords, keys, etc.""",
            default='./secrets/'
        )

    def add_supported_account(self, account) :
        self.log.info(f"Adding support for '{account}' accounts")
        self.supported_accounts[account.account_name] = account

    def run(self) :
        args = self.parser.parse_args()

        secrets = SecretReader(args.secret_directory)

        # There must be a secret matching the house_name. It should define the shape of the house.
        # TODO spec for shape of house JSON
        home = secrets.read(args.home_name)
        self.log.info(f'Shape of home: {home}')

        # TODO add more accounts. Need Hue, Weemo, Amazon, Google. Then Harmony, Nest, other smart devices.
        self.add_supported_account(RingAccount(secrets))

        for account_name in home['accounts'] :
            if account_name in self.supported_accounts :
                self.supported_accounts[account_name].connect()
            else :
                self.log.warn(f"Account type '{account_name}' is not supported.")

if __name__ == '__main__' :
    main()
