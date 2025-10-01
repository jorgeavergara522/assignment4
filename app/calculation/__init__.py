from abc import ABC, abstractmethod
from app.operations import Operations  # <- plural, correct import

class Calculation(ABC):
    def __init__(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Inputs must be numbers")
        self.a = float(a)
        self.b = float(b)

    @abstractmethod
    def get_result(self) -> float: ... # pragma: no cover

class AddCalculation(Calculation):
    def get_result(self) -> float:
        return Operations.addition(self.a, self.b)        # <- addition

class SubtractCalculation(Calculation):
    def get_result(self) -> float:
        return Operations.subtraction(self.a, self.b)     # <- subtraction

class MultiplyCalculation(Calculation):
    def get_result(self) -> float:
        return Operations.multiplication(self.a, self.b)  # <- multiplication

class DivideCalculation(Calculation):
    def get_result(self) -> float:
        return Operations.division(self.a, self.b)        # <- division (raises ValueError on 0)

class CalculationFactory:
    _map = {
        "add": AddCalculation,
        "sub": SubtractCalculation,
        "mul": MultiplyCalculation,
        "div": DivideCalculation,
    }

    @staticmethod
    def create(kind: str, a, b) -> Calculation:
        try:
            cls = CalculationFactory._map[kind.lower()]
        except KeyError:
            raise ValueError("Unknown operation")
        return cls(a, b)
