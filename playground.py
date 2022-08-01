import time

from core.contract import Contract
from core.explorer import etherscan
from core.chains import ethereum

usdt_address = "0xdaC17F958D2ee523a2206206994597C13D831ec7"
usdt = Contract(usdt_address, ethereum)
print(
    "USDT balance of USDT (burned funds):",
    usdt.balanceOf(usdt_address, block=15255547) / 10 ** usdt.decimals(block=15255547),
)

time.sleep(5)

timestamp = int(time.time())
block = etherscan.block.getblocknobytime(timestamp=timestamp, closest="before")
print(block, ethereum.eth.block_number)
