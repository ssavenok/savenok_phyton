input_value = input("Input array or comma separated numbers:")
input_value = input_value.replace("[", "").replace("]", "").replace(" ", "")
numbers = input_value.split(",")
results = []
for number in numbers:
    if int(number) % 3 == 0:
        results.append(str(number))
print(", ".join(results))