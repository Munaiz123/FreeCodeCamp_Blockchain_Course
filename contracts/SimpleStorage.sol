// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract SimpleStorage{
    uint256 favoriteNumber;

    // bool favBool = true;
    // string favString = 'Munaiz';
    // int favInt = -7;
    // address favAddress = "0xB18fAC905F2750047703C72E357F4672f57866bf";
    // bytes32 favByte = 'cat';


    struct People{
        uint256 favoriteNumber;
        string name;
    }

    //DYNAMIC ARRAY ; 
    People[] public people; 

    // STRUCT
    People public Munaiz = People({favoriteNumber:3, name: "Munaiz"});
    mapping(string => uint256) public nameToFavNum;



    // FUNCTIONS / METHODS

    function store(uint256 _favNumber) public {
        favoriteNumber = _favNumber;
    }

    function  retrieve() public view returns (uint256){
        return favoriteNumber;
    }

    function addPerson (string memory _name, uint256 _favNumber) public{
        people.push(People(_favNumber, _name));
        nameToFavNum[_name] = _favNumber;
    }
}

