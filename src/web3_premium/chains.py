from dataclasses import dataclass
from typing import Optional

from web3 import Web3
from web3.middleware import geth_poa_middleware

from .contract import Contract
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
from . import utils


@dataclass
class NativeToken:
    symbol: str
    decimals: int = 18


class Chain(Web3):
    explorer: Optional[Explorer]
    native_token: Optional[NativeToken]

    def contract(chain):
        def _contract(*args, **kwargs):
            return Contract(*args, chain=chain, **kwargs)

        return _contract

    def get_datetime_by_block(chain):
        def _get_datetime_by_block(block):
            return utils.get_datetime_by_block(chain, block)

        return _get_datetime_by_block


def chain_w3(
    rpc, explorer=None, symbol: str = None, decimals=18, poa_middleware=True
) -> Chain:
    w3 = Web3(Web3.HTTPProvider(rpc))
    w3.explorer = explorer
    w3.native_token = NativeToken(symbol, decimals) if symbol else None
    if poa_middleware:
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    w3.contract = Chain.contract(w3)
    w3.get_datetime_by_block = Chain.get_datetime_by_block(w3)

    return w3


ethereum = chain_w3("https://rpc.ankr.com/eth", etherscan, "ETH")
avalanche = chain_w3("https://rpc.ankr.com/avalanche", snowtrace, "AVAX")
fantom = chain_w3("https://rpc.ankr.com/fantom", ftmscan, "FTM")
arbitrum = chain_w3("https://rpc.ankr.com/arbitrum", arbiscan, "ETH")
bsc = chain_w3("https://rpc.ankr.com/bsc", bscscan, "BNB")
optimism = chain_w3("https://rpc.ankr.com/optimism", optimistic_etherscan, "ETH")
polygon = chain_w3("https://rpc.ankr.com/polygon", polygonscan, "MATIC")
