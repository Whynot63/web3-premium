from typing import Optional

from web3 import Web3

from .explorer import (
    Explorer,
    etherscan,
    snowtrace,
    ftmscan,
    arbiscan,
    bscscan,
    optimistic_etherscan,
    polygonscan,
)


class Chain(Web3):
    explorer: Optional[Explorer]


def chain_w3(rpc, explorer=None) -> Chain:
    w3 = Web3(Web3.HTTPProvider(rpc))
    w3.explorer = explorer
    return w3


ethereum = chain_w3("https://rpc.ankr.com/eth", etherscan)
avalanche = chain_w3("https://rpc.ankr.com/avalanche-c", snowtrace)
fantom = chain_w3("https://rpc.ankr.com/fantom", ftmscan)
arbitrum = chain_w3("https://rpc.ankr.com/arbitrum", arbiscan)
bsc = chain_w3("https://rpc.ankr.com/bsc", bscscan)
optimism = chain_w3("https://rpc.ankr.com/optimism", optimistic_etherscan)
polygon = chain_w3("https://rpc.ankr.com/polygon", polygonscan)
