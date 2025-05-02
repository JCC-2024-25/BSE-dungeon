nameeeee = input("WHATS YOUR NAME")
print (f"YOU WILL DIE TODAY {nameeeee}...")

import random
import time

class Player:
    def __init__(self):
        self.max_hp = 120
        self.hp = self.max_hp
        self.attack = 15
        self.defense = 5
        self.stunned = False
        self.buff_turns = 0
        self.heal_cooldown = 0
        self.regen_turns = 0
        self.inventory = {
            "Healing Potion": 2,
            "Bomb": 1,
            "Strength Elixir": 1
        }

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        reduced = max(0, dmg - self.defense)
        self.hp -= reduced
        print(f"You took {reduced} damage! HP: {self.hp}/{self.max_hp}")

    def heal(self):
        if self.inventory["Healing Potion"] <= 0:
            print("You have no Healing Potions!")
            return
        if self.heal_cooldown > 0:
            print(f"Healing is on cooldown for {self.heal_cooldown} more turn(s)!")
            return
        heal_amt = random.randint(25, 35)
        self.hp = min(self.max_hp, self.hp + heal_amt)
        self.inventory["Healing Potion"] -= 1
        self.heal_cooldown = 2
        self.regen_turns = 3
        print(f"You used a Healing Potion and restored {heal_amt} HP!")

    def use_bomb(self, enemy):
        if self.inventory["Bomb"] <= 0:
            print("No bombs left!")
            return
        dmg = random.randint(20, 30)
        enemy.take_damage(dmg)
        self.inventory["Bomb"] -= 1
        print(f"You used a Bomb on {enemy.name}!")

    def use_strength_elixir(self):
        if self.inventory["Strength Elixir"] <= 0:
            print("No elixirs left!")
            return
        self.buff_turns = 3
        self.inventory["Strength Elixir"] -= 1
        print("You used a Strength Elixir! +5 attack for 3 turns.")

    def attack_choice(self, enemy):
        print("\nChoose attack:")
        print("1. Slash (Reliable)")
        print("2. Power Strike (High Damage, Low Accuracy)")
        print("3. Stun Blow (Low Damage, Chance to Stun)")
        choice = input("Your attack: ").strip()
        buffed_atk = self.attack + 5 if self.buff_turns > 0 else self.attack

        if choice == "1":
            dmg = random.randint(buffed_atk - 2, buffed_atk + 3)
            print("You use Slash!")
            enemy.take_damage(dmg)
        elif choice == "2":
            if random.random() < 0.6:
                dmg = random.randint(buffed_atk + 5, buffed_atk + 12)
                print("Power Strike hits!")
                enemy.take_damage(dmg)
            else:
                print("Power Strike missed!")
        elif choice == "3":
            dmg = random.randint(5, 10)
            print("You try to Stun Blow!")
            enemy.take_damage(dmg)
            if random.random() < 0.4:
                print(f"You stunned {enemy.name}!")
                enemy.stunned = True
        else:
            print("Invalid attack. You lose your turn.")

    def use_item(self, enemy):
        print("\nItems:")
        for item, count in self.inventory.items():
            print(f"- {item} x{count}")
        item = input("Which item do you want to use? ").strip().lower()

        if item.startswith("heal"):
            self.heal()
        elif item == "bomb":
            self.use_bomb(enemy)
        elif item.startswith("strength"):
            self.use_strength_elixir()
        else:
            print("Invalid item.")

    def regen(self):
        if self.regen_turns > 0:
            self.hp = min(self.max_hp, self.hp + 5)
            print(f"You regenerate 5 HP. HP: {self.hp}/{self.max_hp}")
            self.regen_turns -= 1

    def end_turn(self):
        if self.heal_cooldown > 0:
            self.heal_cooldown -= 1
        if self.buff_turns > 0:
            self.buff_turns -= 1
        self.regen()

class Enemy:
    def __init__(self, name, hp, atk, special=None):
        self.name = name
        self.hp = hp
        self.attack = atk
        self.special = special
        self.stunned = False

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        self.hp -= dmg
        print(f"{self.name} took {dmg} damage! HP left: {self.hp}")

    def perform_attack(self, player):
        if self.stunned:
            print(f"{self.name} is stunned and skips a turn!")
            self.stunned = False
            return {}

        print(f"{self.name} attacks!")
        base_dmg = random.randint(self.attack - 3, self.attack + 3)
        player.take_damage(base_dmg)

        if self.special and random.random() < self.special["chance"]:
            if self.special["type"] == "bleed":
                print("You're bleeding! You'll take 5 damage for 3 turns.")
                return {"bleed": 3}
            elif self.special["type"] == "weaken":
                print("You've been weakened! -3 attack for 2 turns.")
                return {"weaken": 2}
        return {}

def battle(player, enemy):
    print(f"\n-- A wild {enemy.name} appears! --")
    effects = {"bleed": 0, "weaken": 0}

    while player.is_alive() and enemy.is_alive():
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Item")
        action = input("Action: ").strip()

        if player.stunned:
            print("You're stunned and skip your turn!")
            player.stunned = False
        elif action == "1":
            player.attack_choice(enemy)
        elif action == "2":
            player.use_item(enemy)
        else:
            print("Invalid choice. Turn skipped.")

        if enemy.is_alive():
            new_effects = enemy.perform_attack(player)
            for key in new_effects:
                effects[key] = new_effects[key]

        if effects["bleed"] > 0:
            print("You bleed for 5 damage.")
            player.hp -= 5
            effects["bleed"] -= 1

        player.end_turn()

    if player.is_alive():
        print(f"\nYou defeated {enemy.name}!")
        return True
    else:
        print("You died...")
        return False

def choose_path(level):
    path_a = random.choice([
        Enemy("Bombardiro Crocodilo", 55, 14),
        Enemy("Tung Tung Tung Sahur", 50, 12, special={"type": "bleed", "chance": 0.4}),
        Enemy("Brr Brr Patapim", 60, 13),
    ])
    path_b = random.choice([
        Enemy("Cappucino Assasino", 45, 10, special={"type": "weaken", "chance": 0.5}),
        Enemy("Trippa Troppa Tralala Lirilì Rilà Tung Tung Sahur Boneca Tung Tung Tralalelo Trippi Troppa Crocodina", 40, 16),
        Enemy("Bomboclat Crococlat", 48, 11, special={"type": "bleed", "chance": 0.3}),
    ])

    print(f"\n=== Level {level} ===")
    print(f"A: {path_a.name}")
    print(f"B: {path_b.name}")
    choice = input("Choose path A or B: ").strip().lower()
    return path_a if choice == 'a' else path_b

def dungeon_crawl():
    player = Player()
    for level in range(1, 6):
        enemy = choose_path(level)
        survived = battle(player, enemy)
        if not survived:
            print("Game Over.")
            return
        print(f"Level {level} complete!\n")
        time.sleep(2)

    print("You cleared the dungeon! Victory!")

if __name__ == "__main__":
    dungeon_crawl()
