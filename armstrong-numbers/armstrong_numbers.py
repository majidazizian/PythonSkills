def is_armstrong_number(number):
    temp = 0
    NumberLength = len(str(number))

    for n in str(number):
        temp += pow(int(n), NumberLength)

    return (temp == number)
