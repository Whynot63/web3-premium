from .explorer import Explorer


def fetch_abi(explorer: Explorer, address: str):
    return explorer.contract.getabi(address=address)
