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

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chain_id = 1337
my_address = "0x7eeB11bEa83b3ECB18911E82A4689278286D8171"
private_key = os.getenv("PRIVATE_KEY") # access private key by 'export PRIVATE_KEY=....' from terminal

# Create contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode) # our contract class/object

# get latet transaction
nonce = w3.eth.getTransactionCount(my_address)
gas_price = w3.eth.gas_price


# inorder to deploy a contract, we need to
  # 1) build contract deploy transaction
transaction = SimpleStorage.constructor().buildTransaction({"chainId":chain_id, "from":my_address, "nonce":nonce, "gasPrice":gas_price})
  # 2) sign the transaction
signed_transaction = w3.eth.account.sign_transaction(transaction,private_key=private_key)
  # 3) Send the transaction to the blockchain (local ganache)
transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
# waiting for block confirmation
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)

####################################################################################################################################
# TILL NOW WE'VE DEPLOYED A CONTRACT, NOW WE NEED TO WORK WITH THE CONTRACT
# WE NEED THE CONTRACT ADDRESS & CONTRACT ABI
####################################################################################################################################



print(transaction_receipt)
