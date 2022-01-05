// SPDX_License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;
import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainLink.sol";
import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol"; // importing from NPM package

// this is importing an interface
// interfaces compile down to ABIs, which tells solidiity which funcs can be called on another contract
// Anytime you want to interact with an already deployed smart contrct you need an ABI

//Accept some sort of payment
contract FundMe {
    using SafeMathChainLink for uint256; // Alows us to safely do math where uints arent being wrapped around if the numbers get too big

    //we want to keep track of who sent us money
    mapping(address => uint256) public addressToAmountFunded;

    function fund() public payable {
        //every function call has an associated value with it.
        // When making a transaction you can append an amount of wei with it.
        // can''t break Eth smaller than 1 wei.

        // msg.sender + msg.value are 2 keyworkds that every transaction will have

        //$50
        addressToAmountFunded[msg.sender] += msg.value;
        // what the ETH -> USD Conversion rate
        // use chainlink oracle to connect to an external system for up to date data
    }

    function getVersion() public view returns (uint256) {
        // to interact with an interface contract, it will be the same way
        // we interact with a struct
        AggregatorV3Interface priceFeed = AggregatorV3Interface(
            0x8A753747A1Fa494EC906cE90E9f37563A8AF630e
        );
        return priceFeed.version();
    }

    function getPrice() public view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(
            0x8A753747A1Fa494EC906cE90E9f37563A8AF630e
        );

        // destructuring a tuple here that originally returns 5 vairables.
        (, int256 answer, , , ) = priceFeed.latestRoundData(); // commas are used as place holders for the other variables we dont need
        return uint256(answer * 10000000000);
    }

    function getConversionRate(uint256 ethAmount)
        public
        view
        returns (uint256)
    {
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUSD = (ethPrice * ethAmount) / 1000000000000000000;
        return ethAmountInUSD;
    }
}
