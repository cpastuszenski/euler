<<<<<<< HEAD
_ones_len = {
    1: 3, #'one'
    2: 3, #'two'
    3: 5, #'three'
    4: 4, #'four'
    5: 4, #'five'
    6: 3, #'six'
    7: 5, #'seven'
    8: 5, #'eight'
    9: 4, #'nine'
    10: 3, #'ten'
    11: 6, #'eleven'
    12: 6, #'twelve'
    13: 8, #'thirteen'
    14: 8, #'fourteen'
    15: 7, #'fifteen'
    16: 7, #'sixteen'
    17: 9, #'seventeen'
    18: 8, #'eighteen'
    19: 8, #'nineteen'
=======
# If I wanted to do this as fast as possible, I'd jsut make the dictionaries map directly to word lengths...
# but screw it, this is funnier

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
>>>>>>> 2fb085277bd22d4ab2743177a4f4da38ccc88b67
    }

_tens_len = {
    2: 6, #'twenty
    3: 6, #'thirty
    4: 5, #'forty'
    5: 5, #'fifty'
    6: 5, #'sixty'
    7: 7, #'seventy'
    8: 6, #'eighty'
    9: 6, #'ninety'
    }

def englishify(n):
    if n >= 10000:
        ValueError("Sorry, we don't support the Englishification of numbers larger than 9999")
    elif n < 0:
        ValueError("Sorry, we don't support the Englishification of numbers smaller than 0")
    elif n == 0:
        return 0
    else:
        english = 0

        if n >= 1000:
<<<<<<< HEAD
            english += _ones_len[n / 1000]
            english += 8 #"thousand"
=======
            english += _ones[n / 1000]
            english += "thousand"
>>>>>>> 2fb085277bd22d4ab2743177a4f4da38ccc88b67
            n %= 1000

        if n >= 100:
            english += _ones_len[n / 100]
            if n % 100 == 0:
<<<<<<< HEAD
                english += 7 #"hundred"
            else:
                english += 10 #"hundredand"
=======
                english += "hundred"
            else:
                english += "hundredand"
>>>>>>> 2fb085277bd22d4ab2743177a4f4da38ccc88b67
            n %= 100

        if n >= 20:
            english += _tens_len[n / 10]
            n %= 10

        if n in _ones_len:
            english += _ones_len[n]

        return english


<<<<<<< HEAD
print sum(englishify(i) for i in range(1, 1001))
=======
print sum(len(englishify(i)) for i in range(1, 1001))
>>>>>>> 2fb085277bd22d4ab2743177a4f4da38ccc88b67
