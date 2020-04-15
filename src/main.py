#!/usr/bin/env python3

import sys

from argparse import ArgumentParser
from lib.secret import SecretReader
from lib.account.ring import RingAccount

SUPPORTED_ACCOUNTS = {}

def main() :
    parser = ArgumentParser(description='Central hub for your smart home')
    parser.add_argument(
        '-n', '--home-name',
        help="""The name of your home.
        Must have a matching secret in <secret-directory>/<home-name>.secret that describes the shape of the home.""",
        required=True,
    )
    parser.add_argument(
        '-s', '--secret-directory',
        help="""The directory containing your secret files. Passwords, keys, etc.""",
        default='./secrets/'
    )

    args = parser.parse_args()

    secrets = SecretReader(args.secret_directory)

    # There must be a secret matching the house_name. It should define the shape of the house.
    # TODO spec for shape of house JSON
    home = secrets.read(args.home_name)
    print(f'Shape of home: {home}')

    # TODO add more accounts. Need Hue, Weemo, Amazon, Google. Then Harmony, Nest, other smart devices.
    add_supported_account(RingAccount(secrets))

    for account_name in home['accounts'] :
        if account_name in SUPPORTED_ACCOUNTS :
            SUPPORTED_ACCOUNTS[account_name].connect()
        else :
            print(f"WARN: Account type '{account_name}' is not supported.", file=sys.stderr)


def add_supported_account(account) :
    print(f"Adding support for '{account.account_name}' accounts")
    SUPPORTED_ACCOUNTS[account.account_name] = account

def log_warn(message) :
    print(f'WARN: {message}', file=sys.stderr)

if __name__ == '__main__' :
    main()
