from abc import ABC, abstractmethod


class ConversionStrategy(ABC):
    @staticmethod
    @abstractmethod
    def convert(x):
        pass


class FahrenheitToCelsiusConverter(ConversionStrategy):
    @staticmethod
    def convert(x):
        return (x-32) * 5 / 9


class CelsiusToFahrenheitConverter(ConversionStrategy):
    @staticmethod
    def convert(x):
        return (x * 9 / 5) + 32


result = FahrenheitToCelsiusConverter.convert(32)
print("F to C: ", result)

result2 = CelsiusToFahrenheitConverter.convert(100)
print("C to F: ", result2)
