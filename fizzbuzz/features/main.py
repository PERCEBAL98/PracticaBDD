class FizzBuzz:
    @staticmethod
    def calculates(num):
        result = ""
        if num % 3 == 0:
            result += "Fizz"
        if num % 5 == 0:
            result += "Buzz"
        return result if result else f"{num}"
