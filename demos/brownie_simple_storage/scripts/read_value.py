from brownie import SimpleStorage, accounts, config

# interacting with the deployed / transacted contracts after the fact.

def readContract():
  simpleStorage = SimpleStorage[-1] # always work with the most recent deployment => -1
  #  brownie already know the ABI & Address

  print(simpleStorage.retrieve())





def main():
  readContract()
