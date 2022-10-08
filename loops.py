foods = ["apples","bread", "cheese","milk", "bananas"]

for food in foods:
    if food == "cheese":
        print("you have to but this")
    print(food) 

for food in foods:
    if food == "cheese":
        break
    print(food) 

for food in foods:
    if food == "cheese":
        continue
    print(food) 

for number in range (1,8):
    print(number)

for letter in "hello":
    print(letter)

count = 4

while count <=10:
    print(count)
    count += 1
