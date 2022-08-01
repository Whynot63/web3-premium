from web3 import Web3


def chain_w3(rpc):
    return Web3(Web3.HTTPProvider(rpc))


ethereum = chain_w3("https://rpc.ankr.com/eth")
avalanche = chain_w3("https://rpc.ankr.com/avalanche-c")
fantom = chain_w3("https://rpc.ankr.com/fantom")
arbitrum = chain_w3("https://rpc.ankr.com/arbitrum")
bsc = chain_w3("https://rpc.ankr.com/bsc")
optimism = chain_w3("https://rpc.ankr.com/optimism")
polygon = chain_w3("https://rpc.ankr.com/polygon")
