from brownie import SimpleStorage as SimpleStorageContract, accounts

def test_deploy():
  #Arrange
  account = accounts[0]

  #Acting
  simple_storage = SimpleStorageContract.deploy({"from":account})
  startingVal = simple_storage.retrieve()

  #Asserting
  assert startingVal == 0


def test_updating_storage():
  #Arrange
  account = accounts[0]
  simple_storage = SimpleStorageContract.deploy({"from":account})

  #Acting
  expected = 99
  simple_storage.store(99,{"from":account})

  assert simple_storage.retrieve() == expected



