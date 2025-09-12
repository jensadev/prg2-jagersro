werewolves = [
    {
        "name": "Rulle",
        "health": 100,
        "attack": 15,
        "defense": 10,
    },
    {
        "name": "Luna",
        "health": 120,
        "attack": 10,
        "defense": 15,
    },
    {
        "name": "Fenrir",
        "health": 150,
        "attack": 20,
        "defense": 5,
    }
]

def print_werewolf_info(werewolf: dict) -> None:
    for key, value in werewolf.items():
        print(f"{key}: {value}")


from random import choice
from copy import deepcopy

ww_attacker = deepcopy(werewolves[0])
ww_defender = choice(werewolves)

print_werewolf_info(ww_attacker)
print_werewolf_info(ww_defender)

ww_attacker["health"] -= 40

print_werewolf_info(ww_attacker)

print_werewolf_info(werewolves[0])


# while True:
#     # werewolf fight
#     print(f"{ww_attacker['name']} attackerar {ww_defender['name']}!")
#     ww_attacker['attack'] - ww_defender['defense']
#     ww_defender['health'] -= (ww_attacker['attack'] - ww_defender['defense'])

#     if ww_attacker["health"] < 0:
#         print(f"{ww_attacker['name']} är död och kan inte attackera!")
#         break
#     if ww_defender["health"] < 0:
#         print(f"{ww_defender['name']} är död och kan inte försvara sig!")
#         break

