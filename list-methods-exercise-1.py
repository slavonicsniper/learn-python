# write a program to remove the duplicates in a list

numbers = [2, 5, 5, 3, 7, 7, 4]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)

uniques.sort()
print(uniques)

# my solution

for number in numbers:
    number_count = numbers.count(number)
    if number_count > 1:
        numbers.remove(number)

numbers.sort()
print(numbers)
