number = input("Phone: ")

numbers_words_map = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

output = ''

for digit in number:
    output += numbers_words_map.get(digit, "!") + " "

print(output)
