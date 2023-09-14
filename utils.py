class utils:
    def reversed(number):
        if type(number) == int:
            return int(str(number)[::-1])
        else:
            raise ValueError("Input must be an integer")

    def formatter(number):
        if type(number) == int:
            binary_num = bin(number)[2:]
            octal_num = oct(number)[2:]
            return (binary_num, octal_num)
        else:
            raise ValueError("Input must be an integer")