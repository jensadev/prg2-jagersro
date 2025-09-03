# Fråga användaren om ett namn
# namnet måste vara minst 2 tecken långt
# annars så måste användaren skriva in ett nytt namn

name = ""
while len(name) < 2: # < =
    name = input("Skriv ditt namn: ")

def input_name(prompt = "Skriv ditt namn: ", length = 2) -> str:
    name = ""
    while len(name) < length:
        name = input(prompt)
    return name

name = input_name()
print(name)