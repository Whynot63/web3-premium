import requests
from typing import Callable


class ExplorerError(RuntimeError):
    def __init__(self, message, data) -> None:
        super().__init__(message)

        self.data = data

    def __str__(self) -> str:
        return f"{super().__str__()}.\nReturned result: {self.data}"


class ExplorerAction:
    def __init__(self, module: "ExplorerModule", action: str) -> None:
        self.module = module
        self.action = action

    def __call__(self, **kwargs):
        r = requests.get(
            self.module.explorer.url,
            params={"module": str(self.module), "action": self.action, **kwargs},
        )
        result = r.json()
        if result["status"] != "1":
            raise ExplorerError(result["message"], result["result"])
        return result["result"]


class ExplorerModule:
    def __init__(self, explorer: "Explorer", module: str) -> None:
        self.explorer = explorer
        self.name = module

    def __str__(self) -> str:
        return self.name

    def __getattr__(self, action: str) -> Callable:
        return ExplorerAction(self, action)


class Explorer:
    def __init__(self, url) -> None:
        self.url = url

    def __getattr__(self, module: str) -> ExplorerModule:
        return ExplorerModule(self, module)


etherscan = Explorer("https://api.etherscan.io/api")
snowtrace = Explorer("https://api.snowtrace.io/api")
ftmscan = Explorer("https://api.ftmscan.com/api")
arbiscan = Explorer("https://api.arbiscan.io/api")
bscscan = Explorer("https://api.bscscan.com/api")
optimistic_etherscan = Explorer("https://api-optimistic.etherscan.io/api")
polygonscan = Explorer("https://api.polygonscan.com/api")
