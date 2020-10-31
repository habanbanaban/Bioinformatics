dictionary = {}
with open("genetype.txt") as x:
    data = x.readlines()[1:]
    for line in data:
        key, value = line.split()
        dictionary[key] = value

print(dictionary.get("APOL4"))
print(dictionary.get("RPL19P20"))
print(dictionary.get("CFL1P4"))
