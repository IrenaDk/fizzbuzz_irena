def fizzbuzz(int_arg):
    if not isinstance(int_arg, int):
        raise TypeError("Input argument is not integer")
    if not (int_arg > 0):
        raise ValueError("Input argument is not positive")
    if (int_arg % 3 == 0) and (int_arg % 5 == 0):
        return "FizzBuzz"
    elif int_arg % 3 == 0:
        return "Fizz"
    elif int_arg % 5 == 0:
        return "Buzz"
    else:
        return int_arg

