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
    choice = input("Choose your character: ")
    if choice == 1:
        character = "Wizard"
        my_hp = wizard_hp
        print("You have chosen the character: " + character)
        print("Health: " + my_hp)
    break
    """ if choice == 2:
        character = "Elf"
        my_hp = elf_hp
        print("You have chosen the character: ", character)
        print("Health: ", my_hp)
        break
    if choice == 3:
        character = "Human"
        my_hp = human_hp
        print("You have chosen the character: ", character)
        print("Health: ", my_hp)
        break """
print("Unknown character")