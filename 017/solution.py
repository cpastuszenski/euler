_ones = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    }

_tens = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
    }

def englishify(n):
    if n > 10000:
        ValueError("Sorry, we don't support the Englishification of numbers larger than 10000")
    elif n < 0:
        ValueError("Sorry, we don't support the Englishification of numbers smaller than 0")
    elif n == 0:
        return 'zero'
    else:
        english = ''

        if n >= 1000:
            english += _ones[n / 1000]
            if n % 1000 == 0:
                english += " thousand"
            else:
                english += " thousand "
            n %= 1000

        if n >= 100:
            english += _ones[n / 100]
            if n % 100 == 0:
                english += " hundred"
            else:
                english += " hundred and "
            n %= 100

        if n >= 20:
            english += _tens[n / 10]
            n %= 10

        if n in _ones:
            english += _ones[n]

        return english


print sum(len(englishify(i).replace(" ", "")) for i in range(1, 1001))