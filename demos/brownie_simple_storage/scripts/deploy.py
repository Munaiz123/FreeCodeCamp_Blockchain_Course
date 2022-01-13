
from brownie import accounts, config, SimpleStorage, network
# import os

def deploy_simple_storage():
  print("*****************************************************************************************")
  account = get_account()
  print("Deploying....")
  simple_storage = SimpleStorage.deploy({"from":account}) # always need a "from" key when making a transaction

  print("Storing....")
  transaction =  simple_storage.store(17,{"from":account})
  transaction.wait(1) # wait for transactions to finish


  stored_value = simple_storage.retrieve() # a view function so we dont need "from" key
  print("stored_value =>", stored_value)


def get_account():

  if(network.show_active() == 'development'):
    return accounts[0]  # USING BROWNIE'S BUILT IN GANACHE ACCOUNTS THAT IT RUNS UP UPON INVOKATION
  else:
    return accounts.add(config["wallets"]["from_key"]) # USING brownie-config.yml to get directly from .env file -> don't need to import OS but need import 'config' from brownie
    # return accounts.load('munziTest') # ADDING ACCOUNTS PRIVATE KES THROUGH ECNCRYPTED COMMAND LINES
    # return accounts.add(os.getenv("PRIVATE_KEY"))  # USES .ENV  FILE





def main():
  deploy_simple_storage()
