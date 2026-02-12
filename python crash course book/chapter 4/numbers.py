# 4.3
counter = range(1,21)
for count in counter:
    print(count)

# 4.4  one million
one_mill = range(1, 1000001)
# printing a million takes forever, print proccess same as 4.3

# 4.5 min max sum of one million
print(f"min in one million {min(one_mill)}")
print(f"max number in one million {max(one_mill)}")
print(f"The sum of all numbers in one million is {sum(one_mill)}")

# 4.6  odd numbers
odd_numbers = range (1,21,2)
for number in odd_numbers:
    print(number)

#  4.7 threes
print()
threes = range(3,31,3)
for item in threes:
    print(item)

# 4.8 cubes
cubes = []
for number in range(1,11):
    cubes.append(number**3)
print(cubes)

# 4.9 cubes comprehension
cubes_two = [value **3 for value in range(1,11)]
print(cubes_two)