wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 300
dragon_damage = 50

while True:
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    character = input("Choose your character: ")
    if character == "1" or character == "Wizard" or character == "wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character == "2" or character == "Elf" or character == "elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == "3" or character == "Human" or character == "human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    print("Unknown character")
print("You have chosen the character: " + character)
print("Health = ", my_hp)
print("Damage = ", my_damage)
print()

while True:
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!")
    print("The dragon's hitpoints are now:", dragon_hp)
    print()
    if dragon_hp <= 0:
        print("The dragon has lost the battle.")
        break
    my_hp = my_hp - dragon_damage
    print("The dragon has damaged the", character, "!")
    print("The", character, "'s hitpoints are now:", my_hp)
    print()
    if my_hp <= 0:
        print("The", character, "has lost the battle.")
        break