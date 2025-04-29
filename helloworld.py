import sys

print(sys.version)

print("what is next topic to  study")

if 5 > 2:
  print("Five is greater than two!")

x = 5
y = "John"
print(x)
print(y)

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

x = str("Hello World")
print(x)

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

