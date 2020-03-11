import sys
import re


def cardnumber(n):
    sum = 0
    secondnum = 0
    i = len(n) - 1
    num = 0

    while i >= 0:

        num = int(n[i])

        if secondnum:
            num = num * 2

            if num > 9:
                num = (num % 10) + 1

        sum = sum + num

        secondnum = not secondnum

        i -= 1

    return sum % 10 == 0


if __name__ == "__main__":




    n = str(sys.argv[1])

    if cardnumber(n):
        print("valid")

    else:
        print("invalid")

    #check who the card vendor is
def checkvendor(number):
        number = list(map(int, number))

        digits = []
        for x in range(len(number) - 2, -1, -2):
            digits.append(number[x] * 2)
        for y in range(len(number) - 1, -1, -2):
            digits.append(number[y])

        digits = list(map(int, ''.join(map(str, digits))))
        return sum(digits) % 10 == 0

vendors = {"4": "Visa",
           "5[0-6]": "mastercard"}

number_str = input(" card number : ")
if 12 < len(number_str) < 17 :
    try:
        vendor = next(v for k, v in vendors.items() if re.match(k, number_str))
        if checkvendor(number_str):
            print('this is a valid "%s" card!' % vendor)
        else :
            print('this is not a valid "%s"  card' % vendor)
    except StopIteration:
        print('unknown vendor')
else:
    print("this is not a card number ")


