contract DisasterRelief {
  address public ngo;
  address public owner;

  constructor(address _ngo) {
         owner = msg.sender;
         ngo = _ngo;
     }

     function releaseFunds() public {
         require(msg.sender == owner, "Not authorized");
         payable(ngo).transfer(address(this).balance);
     }
     receive() external payable {}
 }
