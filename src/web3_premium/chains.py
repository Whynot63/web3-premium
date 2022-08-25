from dataclasses import dataclass
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


@dataclass
class NativeToken:
    symbol: str
    decimals: int = 18


class Chain(Web3):
    explorer: Optional[Explorer]
    native_token: Optional[NativeToken]


def chain_w3(rpc, explorer=None, symbol: str = None, decimals=18) -> Chain:
    w3 = Web3(Web3.HTTPProvider(rpc))
    w3.explorer = explorer
    w3.native_token = NativeToken(symbol, decimals) if symbol else None
    return w3


ethereum = chain_w3("https://rpc.ankr.com/eth", etherscan, "ETH")
avalanche = chain_w3("https://rpc.ankr.com/avalanche", snowtrace, "AVAX")
fantom = chain_w3("https://rpc.ankr.com/fantom", ftmscan, "FTM")
arbitrum = chain_w3("https://rpc.ankr.com/arbitrum", arbiscan, "ETH")
bsc = chain_w3("https://rpc.ankr.com/bsc", bscscan, "BNB")
optimism = chain_w3("https://rpc.ankr.com/optimism", optimistic_etherscan, "ETH")
polygon = chain_w3("https://rpc.ankr.com/polygon", polygonscan, "MATIC")
