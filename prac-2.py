horses = [
    {"name": "Secretariat", "age": 3, "breed": "Thoroughbred", "color": "Chestnut"},
    {"name": "Seabiscuit", "age": 4, "breed": "Thoroughbred", "color": "Bay"},
    {"name": "Black Beauty", "age": 5, "breed": "Morgan", "color": "Black"}
]

# for horse in horses:
#     print(f"{horse['name']} är en {horse['age']} år gammal {horse['color']} {horse['breed']}.")

# I reject your reality and substitute my own - Adam Savage


def print_horse_info(horse: dict) -> None:
    # print(f"{horse['name']} är en {horse['age']} år gammal {horse['color']} {horse['breed']}.")
    for key, value in horse.items():
        print(f"{key}: {value}")


for horse in horses:
    print_horse_info(horse)

print_horse_info(horses[1])
