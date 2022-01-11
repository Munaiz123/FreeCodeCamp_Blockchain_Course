
from brownie import accounts

def deploy_simple_storage():
  account = accounts[0]
  # print(account)
  myAccount = accounts.load('freecodecamp-account')
  print(myAccount)


def main():
  deploy_simple_storage()
