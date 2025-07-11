from abc import ABC, abstractmethod
class rbi(ABC):
    @abstractmethod
    def roi(self):
        pass
class icici(rbi):
    def __init__(self, rate):
        self.rate = rate
    def roi(self):
        print(f"Roi of ICICI: {self.rate}%")
class bob(rbi):
    def __init__(self, rate):
        self.rate = rate
    def roi(self):
        print(f"Roi of BOB: {self.rate}%")
i = icici(5)
i.roi()
b = bob(10)
b.roi()

    