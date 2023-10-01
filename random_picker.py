import random

numbers = {
    1: "Aleksandur A",
    2: "Aleksandur D",
    3: "Boris",
    5: "Georgi",
    6: "David",
    7: "Deyan I",
    8: "Deyan S",
    9: "Elena",
    10: "Iva",
    11: "Ivo",
    12: "Ira",
    13: "Yonika",
    14: "Kaloyan",
    15: "Kristiqn",
    16: "Luchezar",
    17: "Luboslav",
    18: "Martin",
    19: "Momchil",
    20: "Petko",
    21: "Petur",
    22: "Plamen",
    23: "Preslav",
    24: "Soner",
    25: "Tea",
    26: "Fatih",
    27: "Hristiqn",
    28: "Tsvetelin",
    29: "Yanitsa",
    30: "Alekzandur",
}

available_numbers = list(numbers.keys())

while available_numbers:
    input("Enter something to get a random")
    
    selected_number = random.choice(available_numbers)
    
    selected_name = numbers[selected_number]
    print(f"Selected number: {selected_number}, Name: {selected_name}")
    
    available_numbers.remove(selected_number)

print("All numbers have been picked.")
