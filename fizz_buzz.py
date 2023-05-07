for item in range(1, 100):
    if item % 3 == 0:
        if item % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif item % 5 == 0:
        print("Buzz")
    else:
        print(item)
