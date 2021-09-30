from brownie import SimpleStorage, accounts, config


def read_contract():
    simple_storage = SimpleStorage[
        -1
    ]  # -1 means most recent deployment of (0, 1, ...,n)
    print(simple_storage.retrieve())


def main():
    read_contract()
