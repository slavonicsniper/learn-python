# list methods

numbers = [5, 2, 1, 5, 5, 7, 4]
numbers.append(20)
numbers.insert(0, 10)
numbers.remove(5)
numbers.pop()

print(numbers)
#print(numbers.clear())
print(numbers.index(2))
#print(numbers.index(50))
print(50 in numbers)
print(numbers.count(5))
numbers.sort()
numbers.reverse()
numbers2 = numbers.copy()
numbers.append(500)
print(numbers)
print(numbers2)
