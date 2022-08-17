import json
from datetime import datetime
from typing import Literal

from .chains import Chain
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


def get_block_by_datetime(
    explorer: Explorer, dt: datetime, closest: Literal["before", "after"] = "before"
):
    return explorer.block.getblocknobytime(
        timestamp=int(dt.timestamp()), closest=closest
    )


def get_datetime_by_block(chain: Chain, block: int):
    return datetime.fromtimestamp(chain.eth.get_block(block).timestamp)
