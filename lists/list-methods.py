numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ["a", "g", "s", "b", "y", "a", "s"]

valMax = min(numbers)
valMin = max(numbers)
letMax = max(letters)
letMin = min(letters)

print(valMax)
print(valMin)

print(letMax) #alfabetik olarak sıralayarak yazar
print(letMin) #alfabetik olarak sıralayarak yazar

val = numbers[3:6]
val = numbers[:3]
val = numbers[4:]

numbers[4] = 40

numbers.append(49)
numbers.append(59)
numbers.insert(3 , 78)
numbers.insert(-1 , 52)

# numbers.pop()
# numbers.pop(0)
# numbers.pop(-1)
# numbers.remove(49)

numbers.sort()
numbers.reverse()

letters.sort()
letters.reverse()

print(numbers)
print(letters)

print(len(numbers))
print(len(letters))

print(numbers.count(10))
print(letters.count("a"))

numbers.clear()
print(numbers)