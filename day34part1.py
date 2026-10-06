chaos_level = 0
snuck_food = False
saved_during_chaos = False

def midnight():
    print("\nIt is midnight.")
    print("1 - Investigate")
    print("2 - Go back to bed")

    choice = input("Choose: ")

    if choice == "1":
        snuck_food == True
        return "hallway"
    else:
        return "bedtime"

def hallway():
    global chaos_level

    print("\nThere is chicken on the counter.")
    print("1 - Steal")
    print("2 - Leave it")

    choice = input("Choose: ")

    if choice == "1":
        chaos_level += 1
        return "morning"
    else:
        return "morning"
    
def scratch_or_not():
    global chaos_level
    if chaos_level == 0:
        print("Oreo sprints away, mom chuckles. She gets up to make your food.")
    elif chaos_level == 1:
        print("Mom looks slightly suspicious.")
    else:
        print("Mom is watching you carefully.")
    if snuck_food:
        print("Mom is making your daily breakfast. Theres chicken on the counter.. Again.")
    else:
        print("Mom is making your daily breakfast. Theres chicken on the counter.")
    print("1 - Steal\n 2 - Wait for your own food.")

    choice = input("Choose: ")

    if choice == "1":
        return "steal"
    elif choice == "2":
        return "peace"

def morning():
    global chaos_level
    global saved_during_chaos

    print("It's the next day. Mom is approaching.")
    print("1 - Stay still\n 2 - Run away")
    choice = input("Choose: ")
    if choice == "1":
        if snuck_food == True:
            return "chicken_ending"
        else:
            return "peace"
    elif choice == "2":
        chaos_level += 1
        if  saved_during_chaos == True and chaos_level >= 2:
            return "secret_ending"
        else:
            return "scratch_or_not"


# --------ENDINGS--------

def secret_ending():
    print("\nMom turns slowly.")
    print("She knew. She always knew.")
    print("ENDING: Watched From The Shadows.")
    return "end"

def chicken_ending():
    print("Mom catches you with chicken on your paws.")
    print("\nENDING: Chicken paws.")
    return "end"


def bedtime():
    print("Mom sees you awake.")
    print("\nENDING: Up past bedtime.")
    return "end"

def peace():
    print("Oreo decides to be a good cat for once.")
    print("\n ENDING: Playing it safe.")
    return "end"

def steal():
    print("Oreo tries to snag a piece of chicken with his paw, he gets caught red handed.")
    print("\nENDING: Stealer")
    return "end"

# --------------

def load_game():
    global chaos_level
    global saved_during_chaos

    try:
        with open("save.txt", "r") as file:
            lines = file.readlines()

            scene_name = lines[0].strip()
            chaos_level = int(lines[1].strip())
            saved_during_chaos = lines[2].strip() == "True"

            print("Game loaded.")
            return scene_name

    except FileNotFoundError:
        print("No save file found.")
        return "midnight"

scenes = {
    "midnight": midnight,
    "hallway": hallway,
    "morning": morning,
    "scratch_or_not": scratch_or_not,
    "chicken_ending": chicken_ending,
    "bedtime": bedtime,
    "peace": peace,
    "steal": steal,
    "secret_ending": secret_ending,
}

def main():
    print("1 - New Game")
    print("2 - Load Game")
    start_choice = input("Choose: ")

    if start_choice == "2":
        current_scene = load_game()
    else:
        current_scene = "midnight"

    while current_scene != "end":
        print("Type 'save' anytime to save.")

        user_input = input("> ")

        if user_input == "save":
            save_game(current_scene)
            continue

        current_scene = scenes[current_scene]()


def save_game(scene_name):
    global saved_during_chaos
    global chaos_level

    if chaos_level > 0:
        saved_during_chaos = True

    with open("save.txt", "w") as file:
        file.write(scene_name + "\n")
        file.write(str(chaos_level) + "\n")
        file.write(str(saved_during_chaos))

    print("Game saved.")




if __name__ == "__main__":
    main()

