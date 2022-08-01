from .chains import (
    ethereum,
    avalanche,
    fantom,
    arbitrum,
    bsc,
    optimism,
    polygon,
)
from .explorer import (
    etherscan,
    snowtrace,
    ftmscan,
    arbiscan,
    bscscan,
    optimistic_etherscan,
    polygonscan,
)


CHAIN_TO_EXPLORER = {
    ethereum: etherscan,
    avalanche: snowtrace,
    fantom: ftmscan,
    arbitrum: arbiscan,
    bsc: bscscan,
    optimism: optimistic_etherscan,
    polygon: polygonscan,
}
