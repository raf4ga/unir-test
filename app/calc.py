import app, math


class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def substract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('Usuario no tiene permisos')

        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("División por cero no es posible")

        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        return x ** y
    
    def square(self, x):
        self.check_types(x, 2)
        self.check_non_negative(x)
        return math.sqrt(x)
    
    def common_logarithm(self, x):
        self.check_types(x, 10)
        self.check_non_negative(x)
        return math.log10(x)

    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parametros deben ser numeros")

    def check_non_negative(self, x):
        if x < 0:
            raise TypeError("Logaritmo comun de un número negativo no es posible")


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
