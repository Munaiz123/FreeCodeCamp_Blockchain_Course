// SPDX-License_Identifier: MIT

pragma solidity ^0.6.0;
import "./SimpleStorage.sol";

contract StorageFactor is SimpleStorage { //Solidity inheritance key word = "is"


    // make an array where you can keep track of all of the simple storages we are creating
    SimpleStorage[] public simpleStorageArray;

    function createSimpleStorageContract() public {
        // creating a new object  of type "SimpleStorage"
        SimpleStorage simpleStorage = new SimpleStorage();
        simpleStorageArray.push(simpleStorage);

    }

    function sfStore(uint256 _simpleStorageIndex, uint256 _simpleStorageNumber) public{
        // whenever interacting with a contract you need the Address + ABI
        SimpleStorage(address(simpleStorageArray[_simpleStorageIndex])).store(_simpleStorageNumber);
    }

    function sfRetrieve(uint256 _ssIndex) public view returns(uint256){
        return SimpleStorage(address(simpleStorageArray[_ssIndex])).retrieve();
    }

} //Once we deploy this StorageFactory Contract, we can create the SimpleStorage Contract,
    // save them in an array and also call the created SimpleStorage Contract methods
