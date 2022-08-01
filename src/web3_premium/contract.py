from eth_utils import is_hex_address, to_checksum_address
from web3 import Web3

from .utils import fetch_abi
from .mappings import CHAIN_TO_EXPLORER


class Contract:
    def __init__(self, address, chain: Web3) -> None:
        self.address = to_checksum_address(address)
        self.explorer = CHAIN_TO_EXPLORER[chain]
        self.abi = fetch_abi(self.explorer, address)
        self._contract = chain.eth.contract(self.address, abi=self.abi)

    def __getattr__(self, method_name):
        def fn(*args, block="latest", **kwargs):
            args = [to_checksum_address(a) if is_hex_address(a) else a for a in args]
            kwargs = {
                k: to_checksum_address(v) if is_hex_address(v) else v
                for k, v in kwargs.items()
            }

            return self._contract.functions[method_name](*args, **kwargs).call(
                block_identifier=block
            )

        return fn
