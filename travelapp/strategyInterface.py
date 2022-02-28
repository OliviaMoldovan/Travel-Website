from .bookingStrategy import *


class Context:
    strategy: Strategy

    def setStrategy(self, strategy: Strategy = None) -> None:

        if strategy is not None:
            self.strategy = strategy

        else:
            self.strategy = Default(0, 0, 0, 0, 0)

    def executeStrategy(self) -> str:
        return self.strategy.execute()
