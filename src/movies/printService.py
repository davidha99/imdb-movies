from typing import List
# Context class for the Strategy pattern
class printService:
    def __init__(self, printOrder) -> None:
        self.printOrder = printOrder

    def print(self) -> List:
        return self.printOrder.printList()