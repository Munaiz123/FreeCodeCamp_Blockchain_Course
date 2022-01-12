
from brownie import accounts, config, SimpleStorage
# import os

def deploy_simple_storage():
  print("*****************************************************************************************")
  account = accounts[0] # USING BROWNIE'S BUILT IN GANACHE ACCOUNTS THAT IT RUNS UP UPON INVOKATION
  print("Deploying....")
  simple_storage = SimpleStorage.deploy({"from":account}) # always need a "from" key when making a transaction
  print(simple_storage)


  # myAccount = accounts.load('munziTest') # ADDING ACCOUNTS PRIVATE KES THROUGH ECNCRYPTED COMMAND LINES

  # myAccount = accounts.add(os.getenv("PRIVATE_KEY"))  # USES .ENV  FILE

  # myAccount = accounts.add(config["wallets"]["from_key"]) USING brownie-config.yml to get directly from .env file -> don't need to import OS but need import 'config' from brownie
  # print(myAccount)



def main():
  deploy_simple_storage()
