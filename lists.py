#lisis

demo_list =[1, "hello", 1.14, True, [1, 2, 3]]
number_list = list((1,2,3,4))
colors = ["red", "blue", "violet"]
print(number_list)

r = list(range(0,1000))
print(r)

print(len(colors))
print(colors[2])
print("red" in colors)

print(colors)
colors[1] = "yellow"
print(colors)

# methods
print(dir(colors))

colors.append("violet")
#colors.append(("yellow","black"))
print(colors)

colors.extend(("yellow","black"))
print(colors)

colors.insert(-1,"pink")
print(colors)

colors.pop()
print(colors)

colors.remove("violet")
print(colors)

colors.clear()
print(colors)

colors = ["red", "blue", "violet"]

colors.sort()
print(colors)

colors.sort(reverse=1)
print(colors)

print(colors.index("blue"))
print(colors.count("red"))