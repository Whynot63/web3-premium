# web3-premium
Data Science friendly wrapper for web3py


## Explorers wrapper

Usage: `<explorer>.<module>.<action>(<params>)`  
List of modules and module actions you can get from explorer documentation (etherscan, for example: https://docs.etherscan.io/api-endpoints/accounts)

```python
import time

from web3_premium.explorer import etherscan


timestamp = int(time.time())
etherscan.block.getblocknobytime(timestamp=timestamp, closest="before")
```

You can also add new explorer, which support etherscan/blockscout api format, for example:
```python
import time

from web3_premium.explorer import Explorer


timestamp = int(time.time())
andromeda = Explorer("https://andromeda-explorer.metis.io/api")
andromeda.block.getblocknobytime(timestamp=timestamp, closest="before")
```

## Web3 smart contracts wrapper
Basic example with pure web3:
```python
# We wanna to know, how many USDT at ethereum holds zero address (0x00000....) at 01.08.2022 (block 15253306)
from web3 import Web3

BLOCK = 15253306

w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))
usdt_abi = ...  # some big json
usdt = w3.eth.contract(
    Web3.toChecksumAddress("0xdaC17F958D2ee523a2206206994597C13D831ec7"), abi=usdt_abi
)
burnedUsdt = usdt.functions.balanceOf(
    "0x0000000000000000000000000000000000000000"
).call(block_identifier=BLOCK)
```

With web3-premium:
```python
# We wanna to know, how many USDT at ethereum holds zero address (0x00000....) at 01.08.2022 (block 15253306)
from web3_premium.chains import ethereum
from web3_premium.contract import Contract

BLOCK = 15253306

usdt = Contract("0xdaC17F958D2ee523a2206206994597C13D831ec7", ethereum)
burnedUsdt = usdt.balanceOf("0x0000000000000000000000000000000000000000", block=BLOCK)



