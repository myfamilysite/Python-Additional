fruits = ["apples", "pears"]
taste = ["sweet", "sour"]

for index, (fruit, t) in enumerate(zip(fruits, taste), start=1):
    print(f"{index}. {fruit} is {t}")