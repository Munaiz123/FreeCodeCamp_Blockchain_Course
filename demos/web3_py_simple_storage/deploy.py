from solcx import compile_standard, install_solc
import json
from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

# compile our soiditt
install_solc("0.6.0")
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.6.0",
)

with open("complied_code.json", "w") as file:
    json.dump(compiled_sol, file)


# Get byte code + abi
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# Local simulated blockchain -> Ganache (it'll be our Javascript VM for our local machine)
# Connecting to Ganache


url = "https://eth-rinkeby.alchemyapi.io/v2/3eKvx-lDHc9ttQoRliwGvCen-0QZkmbd"
# url = "HTTP://127.0.0.1:8545" # local URL

w3 = Web3(Web3.HTTPProvider(url))

chain_id = 4
# chain_id = 1337 # local chain_id

my_address = "0xB18fAC905F2750047703C72E357F4672f57866bf"
# my_address = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1" # my local ganache determinisitic address

private_key = os.getenv("PRIVATE_KEY") # access private key by 'export PRIVATE_KEY=....' from terminal
#  dont forget to run 'source .env' in terminla to overwrite any variables exported to the terminal


# Create contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode) # our contract class/object

# get latet transaction
nonce = w3.eth.getTransactionCount(my_address)
gas_price = w3.eth.gas_price


# inorder to deploy a contract, we need to:

  # 1) build contract deploy transaction
transaction = SimpleStorage.constructor().buildTransaction({"chainId":chain_id, "from":my_address, "nonce":nonce, "gasPrice":gas_price})
  # 2) sign the transaction
signed_transaction = w3.eth.account.sign_transaction(transaction,private_key=private_key)
  # 3) Send the transaction to the blockchain (local ganache)
print('Deploying contract ....')
transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
# waiting for block confirmation
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
print('Deployed!')

####################################################################################################################################
# TILL NOW WE'VE DEPLOYED A CONTRACT, NOW WE NEED TO WORK WITH THE CONTRACT
####################################################################################################################################

# WE NEED THE CONTRACT ADDRESS & CONTRACT ABI
simple_storage_contract = w3.eth.contract(address=transaction_receipt.contractAddress, abi=abi)
# when we make transactions on the blockchain, there are actually two ways you can interact with them:
  # 1) Call -> simulate making the call and getting a return value - doesn't make an on chain state change even if in solidity the function you made is supposed to. it just simulates it. (Blue buttons in remix)
  # 2) Transact -> actually makes an on chain state change even if in solidity it doesn't, like retrieve. (Orange buttons in remix)

print(simple_storage_contract.functions.retrieve().call()) # calling the function defined in smart contract - .sol file


# inorder to deploy a contract, we need to (part II):

print('Updating contract with fave number...')
store_transaction = simple_storage_contract.functions.store(17).buildTransaction({
  "chainId":chain_id, "from":my_address, "nonce":nonce +1, "gasPrice":gas_price # created transaction
})
signed_store_transaction = w3.eth.account.sign_transaction(store_transaction, private_key=private_key) # signed transaction
send_store_transaction = w3.eth.send_raw_transaction(signed_store_transaction.rawTransaction)  # sent signed transaction transaction
print('Updated!')
store_transaction_receipt = w3.eth.wait_for_transaction_receipt(send_store_transaction) # waiting for transaction to finish


print(simple_storage_contract.functions.retrieve().call())
