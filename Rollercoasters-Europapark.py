# Recommend a rollercoaster from Europa park that the person would most likely enjoy to do.

def ask_yes_no(question):
    while True:
        answer = input(question + " (yes/no): ").strip().lower()
        if answer in ("yes", "y"):
            return True
        elif answer in ("no", "n"):
            return False
        else:
            print("Please answer with yes or no.")

def ask_choice(question, choices):
    while True:
        answer = input(f"{question} ({'/'.join(choices)}): ").strip().lower()
        if answer in choices:
            return answer
        print("Invalid choice, try again.")
        

def start():
    print("\nHello and welcom to the Europa park Rollercoaster Recommender. ")
    print("Europa Park has about 14 roller coasters, and you probably wont be able to ride them all.")
    print("They also vary widely in type: fast, high, with inversions and loops, or less intense and more fun.")
    print("I help you find the one you definitely want to ride.")
    print("\nJust answer the questions and you'll quickly find out 😀.\n")

    
def length_check():
    while True:
        try:
            return int(input("How tall are you in centimeters?: "))
        except ValueError:
            print("Enter a valid number.")
    

def young_kids_path():
    if ask_yes_no("Do you want butterflies in your stomach?"):
        if ask_yes_no("Do you like to get soaked?: "):
            return "Atlantica Supersplash"    
        system = ask_choice(
            "Would you prefer something with a launch or nothing that rides down a slope?",
            ["launch", "slope"]
        )
        return "Alpen Express" if system == "launch" else "Pegasus"
    return "Ba-a-a Express"



def kids_path():
    if ask_yes_no("Do you look for an intense rollercoaster?: "):
        if ask_yes_no("is this your first roller coaster?"):
            funny_path()
        else:
            return "Wodan"
    return funny_path()
        


def intens_path():
    if ask_yes_no("Do you look for an intense rollercoaster?: "):
        if ask_yes_no("Oke, lets go 🔥! Do you look for loops and inversions?: "):
            if ask_yes_no("Great, are you comfortable with inversions?: "):
                return "Voltron"
            return "Blue Fire"
        if ask_yes_no("Do you want to try something where you spin around and go backwards while riding?"):
            return "Euro-Mir"
        return "Wodan"
    return funny_path()
        

def high_path():
    if ask_yes_no("Do you want to try something really fast and incredibly high? About 70 meters in the air and a lot of air time?: "):
        return "Silverstar"
    return intens_path()
        
        
def funny_path():
        if ask_yes_no("Are you looking for a funny roller coaster?: "):
            if ask_yes_no("Are you looking for something that is indoor?: "): 
                indoor = ask_choice(
                    "Do you want a real coaster or more a darkride like Coaster?",
                    ["darkride", "real coaster"]
                )
                return "Arthur" if indoor == "darkride" else "Cancan Coaster"
            
            
            if ask_yes_no("Do you like to get soaked?: "):
                return soaked_path()
            
            rail = ask_choice(
                "Do you want a bobsled-like roller coaster or a wild mouse roller coaster with tight turns and drops?",
                ["bobsled", "wild mouse"]
            )
            return "Scheizer Bobbahn" if rail == "bobsled" else "Matterhorn blitz"
        
        return "Alpen Express"


def soaked_path():
    choice = ask_choice(
        "One big splash or a coaster track?",
        ["splash", "track"]
    )
    return "Atlantica Supersplash" if choice == "splash" else "Poseidon"

def recommendation():    
    start()
    length = length_check()
    
    if length < 100:
        print("\nSorry, you are too short for these rollercoasters ❌.")
        return
    
    if length < 120:
        coaster = young_kids_path()
    
    elif length < 130:
        coaster = kids_path()
        
    elif length < 140:
        coaster = intens_path()
        
    elif length >= 140 and length < 195:
        coaster = high_path()
        
    if length > 195:
        print("\nSorry, you are too long for these rollercoasters ❌.")
        if length > 272:
            print("\nDid you inform Guinness World Records about that❗️?\n")
        return

    print("\n Your perfect rollercoaster is:")
    print(f" {coaster} 🎢")
    print("\nHave an amazing day at Europa-Park 🎡!\n")


if __name__ == "__main__":
    recommendation()