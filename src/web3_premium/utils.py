import json

from .explorer import Explorer


def fetch_abi(explorer: Explorer, address: str):
    contract_info = explorer.contract.getsourcecode(address=address)[0]
    abi = json.loads(contract_info["ABI"])
    if contract_info["Proxy"] == "1":
        implementation_info = explorer.contract.getsourcecode(
            address=contract_info["Implementation"]
        )[0]
        abi = json.loads(implementation_info["ABI"])

    return abi
