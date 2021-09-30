from brownie import accounts, config, SimpleStorage, network

# import ps


def deploy_simple_storage():
    # account = accounts[0]
    # print(account)
    # account = accounts.load("freecodecamp-account")
    # print(account)
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["from_key"])

    # works only for Ganache
    # account = accounts[0]
    account = get_account()

    # Create Contract from SOL contract
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)  # wait for how many blocks -> 1 in this case
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
