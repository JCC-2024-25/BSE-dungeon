import sys

# GAME START
name = input("ENTER YOUR NAME: ").upper()

print("YOU START IN A DARK ROOM. SUDDENLY, THE LIGHTS TURN ON. YOU SEE A SHADOW. HE INTRODUCES HIMSELF AS DIDDY.")
print(f"DIDDY: HELLO THERE {name}...")

words = input("WHAT WOULD YOU LIKE TO SAY TO DIDDY: ").upper()
print(f"YOU: {words}.")
print("DIDDY: I KNOW EVERYTHING...")
print("{PORTAL APPEARS}")
print("YOU: (GASP)!")
print("YOU HAVE NOW ENTERED THE DUNGEON")
print("...")

wordssec = input("YOU WHISPER TO YOURSELF: ").upper()
print("RUMBLE...RUMBLE...")

# ========== STAGE 1: SPIDER ==========
print("YOU HAVE ENTERED THE FIRST DOOR...")
print("A GIANT SLEEPING SPIDER BLOCKS YOUR PATH.")
print("YOU SEE A SWORD ON THE WALL. YOU GRAB IT.")
print("SPIDER:... SPIDER:..GRAGGGGHHHHHH!")
print("YOU HAVE ENTERED A FIGHT SCENE.")

choice = input("WHAT WOULD YOU LIKE TO DO? (BACK KICK, STAB, SLASH, DANCE): ").strip().lower()

if choice == "back kick":
    print("THE SPIDER AVOIDS YOUR ATTACK AND POUNCES!")
    choice2 = input("QUICK! (DODGE LEFT, DODGE RIGHT, COUNTER PUNCH, STICK YOUR SWORD OUT): ").strip().lower()
    
    if choice2 == "dodge left":
        print("YOU DODGE LEFT, BUT THE SPIDER ANTICIPATES. IT BITES YOU!")
        print("YOU DIED")
        sys.exit()
    elif choice2 == "dodge right":
        print("YOU ROLL RIGHT AND ESCAPE THE ATTACK!")
        choice3 = input("NOW WHAT? (SLASH AT ITS LEGS, THROW SWORD, RUN AWAY): ").strip().lower()
        if choice3 == "slash at its legs":
            print("YOU CUT OFF TWO LEGS! SPIDER DIES!")
        elif choice3 == "throw sword":
            print("YOU MISS! SPIDER ATTACKS! YOU DIED!")
            sys.exit()
        elif choice3 == "run away":
            print("YOU TRY TO RUN BUT SPIDER CHASES YOU. YOU DIED.")
            sys.exit()
    elif choice2 == "counter punch":
        print("PUNCHING A SPIDER? BAD IDEA. YOU DIED.")
        sys.exit()
    elif choice2 == "stick your sword out":
        print("SPIDER IMPALES ITSELF! YOU WIN!")
    else:
        print("INVALID MOVE. SPIDER ATTACKS. YOU DIED.")
        sys.exit()

elif choice == "stab":
    print("YOU QUICKLY STAB THE SPIDER!")
    choice4 = input("FINISH IT? (STAB AGAIN, DODGE, YELL): ").strip().lower()
    if choice4 == "stab again":
        print("YOU FINISH IT OFF! THE SPIDER DIES!")
    elif choice4 == "dodge":
        print("SPIDER DOESN'T ATTACK. YOU LOOK SILLY. THEN IT BITES YOU. YOU DIED.")
        sys.exit()
    elif choice4 == "yell":
        print("YOUR SCREAM CONFUSES IT. YOU WIN!")
    else:
        print("INVALID MOVE. SPIDER ATTACKS. YOU DIED.")
        sys.exit()

elif choice == "slash":
    print("SLOW SLASH! SPIDER MOVES!")
    choice5 = input("QUICK! (SWITCH HANDS, SWING WIDER, JUMP BACK): ").strip().lower()
    if choice5 == "switch hands":
        print("YOU CONFUSE IT AND STRIKE! WIN!")
    elif choice5 == "swing wider":
        print("TOO SLOW. SPIDER BITES YOU. YOU DIED.")
        sys.exit()
    elif choice5 == "jump back":
        print("YOU DODGE, BUT SPIDER HUNTS YOU DOWN. YOU DIED.")
        sys.exit()
    else:
        print("INVALID MOVE. SPIDER ATTACKS. YOU DIED.")
        sys.exit()

elif choice == "dance":
    print("YOU START DANCING...")
    choice6 = input("NOW WHAT? (CONTINUE DANCING, THROW SWORD, RUN PAST IT): ").strip().lower()
    if choice6 == "continue dancing":
        print("YOUR MOVES MELT ITS BRAIN. YOU WIN!")
    elif choice6 == "throw sword":
        print("BULLSEYE! SPIDER DIES!")
    elif choice6 == "run past it":
        print("SPIDER CATCHES YOU. YOU DIED.")
        sys.exit()
    else:
        print("INVALID MOVE. SPIDER ATTACKS. YOU DIED.")
        sys.exit()
else:
    print("INVALID MOVE. SPIDER ATTACKS. YOU DIED.")
    sys.exit()

# ========== STAGE 2: GOBLIN ==========
print("\nYOU WALK INTO THE NEXT ROOM...")
print("A SMALL GOBLIN GUARDS THE EXIT, SHARP TEETH FLASHING.")
print("IT WIELDS TWO DAGGERS.")

choice = input("WHAT WOULD YOU LIKE TO DO? (CHARGE, THROW ROCK, INSULT, HIDE): ").strip().lower()

if choice == "charge":
    print("YOU RUSH AT THE GOBLIN!")
    choice2 = input("(DODGE LEFT, DODGE RIGHT, TACKLE, SLASH): ").strip().lower()
    if choice2 == "dodge left":
        print("YOU EVADE A DAGGER AND STRIKE! GOBLIN DEAD!")
    elif choice2 == "dodge right":
        print("THE GOBLIN ANTICIPATES AND STABS YOU. YOU DIED.")
        sys.exit()
    elif choice2 == "tackle":
        print("YOU SMASH THE GOBLIN INTO A WALL! VICTORY!")
    elif choice2 == "slash":
        print("GOBLIN DODGES. COUNTER ATTACKS. YOU DIED.")
        sys.exit()
    else:
        print("INVALID MOVE. YOU DIED.")
        sys.exit()

elif choice == "throw rock":
    print("YOU THROW A ROCK!")
    choice3 = input("(AIM FOR HEAD, AIM FOR LEGS, FAKE THROW): ").strip().lower()
    if choice3 == "aim for head":
        print("HEADSHOT! GOBLIN DEAD!")
    elif choice3 == "aim for legs":
        print("GOBLIN STUMBLES! EASY KILL!")
    elif choice3 == "fake throw":
        print("GOBLIN CHARGES YOU! YOU DIED.")
        sys.exit()
    else:
        print("INVALID MOVE. YOU DIED.")
        sys.exit()

elif choice == "insult":
    print("YOU HURL AN INSULT!")
    print("GOBLIN GETS ENRAGED AND RUSHES!")
    choice4 = input("(COUNTER ATTACK, RUN, PRETEND TO SURRENDER): ").strip().lower()
    if choice4 == "counter attack":
        print("YOU SLICE THE GOBLIN AS IT ATTACKS!")
    elif choice4 == "run":
        print("GOBLIN CHASES YOU DOWN. YOU DIED.")
        sys.exit()
    elif choice4 == "pretend to surrender":
        print("GOBLIN GETS TOO CLOSE... BAD IDEA. YOU DIED.")
        sys.exit()
    else:
        print("INVALID MOVE. YOU DIED.")
        sys.exit()

elif choice == "hide":
    print("YOU TRY TO HIDE...")
    print("THE GOBLIN SMELLS YOU OUT. YOU DIED.")
    sys.exit()

else:
    print("INVALID MOVE. GOBLIN ATTACKS. YOU DIED.")
    sys.exit()

# ========== STAGE 3: BAT SWARM ==========
print("\nYOU ENTER A DARK TUNNEL...")
print("A SWARM OF BATS DESCENDS!")

choice = input("WHAT WILL YOU DO? (RUN, DUCK, SWING SWORD, SCREAM): ").strip().lower()

if choice == "run":
    print("BATS FOLLOW AND ATTACK!")
    print("YOU DIED.")
    sys.exit()
elif choice == "duck":
    print("YOU AVOID MOST OF THEM. YOU ESCAPE!")
elif choice == "swing sword":
    print("YOU SWING WILDLY, HITTING MANY BATS!")
    print("YOU CLEAR A PATH AND MOVE ON!")
elif choice == "scream":
    print("YOUR SCREAM CONFUSES THE BATS! YOU ESCAPE!")
else:
    print("INVALID MOVE. BATS OVERWHELM YOU. YOU DIED.")
    sys.exit()

# ========== STAGE 4: SKELETON KING ==========
print("\nA MASSIVE THRONE ROOM...")
print("THE SKELETON KING RISES FROM HIS SEAT.")

choice = input("WHAT WILL YOU DO? (BOW, ATTACK, INSULT, RUN): ").strip().lower()

if choice == "bow":
    print("HE LAUGHS AT YOUR FOOLISHNESS. HE CRUSHES YOU. YOU DIED.")
    sys.exit()
elif choice == "attack":
    print("YOU RUSH THE KING!")
    choice2 = input("(AIM FOR HEAD, AIM FOR CHEST, AIM FOR LEGS): ").strip().lower()
    if choice2 == "aim for head":
        print("YOU DESTROY HIS SKULL! HE COLLAPSES!")
    elif choice2 == "aim for chest":
        print("HE IGNORES YOUR ATTACK. COUNTERS. YOU DIED.")
        sys.exit()
    elif choice2 == "aim for legs":
        print("YOU BREAK HIS LEGS! HE FALLS! YOU WIN!")
    else:
        print("INVALID MOVE. YOU DIED.")
        sys.exit()

elif choice == "insult":
    print("HE ROARS WITH ANGER! BATTLE BEGINS!")
    print("YOU OUTSMART HIM AND WIN!")
elif choice == "run":
    print("THERE IS NOWHERE TO RUN. YOU DIED.")
    sys.exit()

else:
    print("INVALID MOVE. YOU DIED.")
    sys.exit()

# ========== FINAL BOSS: DIDDY ==========
print("\nYOU RETURN TO THE DARK ROOM...")
print("DIDDY STANDS BEFORE YOU... STRONGER THAN EVER.")

choice = input("FINAL MOVE! (ATTACK, TALK, OFFER HANDSHAKE, CHARGE PORTAL): ").strip().lower()

if choice == "attack":
    print("DIDDY DODGES EVERYTHING. YOU ARE DESTROYED.")
    print("YOU DIED.")
    sys.exit()
elif choice == "talk":
    print("YOU SPEAK FROM THE HEART. DIDDY SPARES YOU.")
    print("YOU WIN! THE DUNGEON CRUMBLES...")
elif choice == "offer handshake":
    print("DIDDY ACCEPTS... THEN PULLS YOU INTO THE PORTAL.")
    print("NEW ADVENTURE BEGINS...")
elif choice == "charge portal":
    print("YOU JUMP INTO THE PORTAL BEFORE DIDDY CAN STOP YOU!")
    print("YOU ESCAPE!")
else:
    print("INVALID MOVE. DIDDY ENDS YOU. YOU DIED.")
    sys.exit()

