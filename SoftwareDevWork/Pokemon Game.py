#Pokemon Game
import tkinter as tk
import random
from tkinter import messagebox

pokemon_stats = {
    "Charmander": {"health": 100, "power": 80},
    "Bulbasaur": {"health": 100, "power": 75},
    "Squirtle": {"health": 100, "power": 70},
    "Pikachu": {"health": 100, "power": 90}
}
pokemon_enemy_stats = {
    "Lulcario": {"health": 150, "power": 80},
    "Snorlax": {"health": 300, "power": 30},
    "Weedle": {"health": 75, "power": 45},
    "MewTwo": {"health": 90, "power": 80}
}
#modified this function to conjoin the enemy and pokemon dictionaries.
#checks whether enemy or player to determine which dictionary to use.
def display_stats(pokemon, is_enemy=False):
    if is_enemy:
        pokemon_stats_dict = pokemon_enemy_stats
    else:
        pokemon_stats_dict = pokemon_stats
    if pokemon in pokemon_stats_dict:
        health = pokemon_stats_dict[pokemon]["health"]
        power = pokemon_stats_dict[pokemon]["power"]
        result_label.config(text=f"{pokemon}: Health: {health}, Power: {power}")

#in this attack funciton, first determines whether or not enemy/player, 
#then using random damage value to subtract from pokemons health variable.
def attack(pokemon, is_enemy=False):
    if is_enemy:
        pokemon_stats_dict = pokemon_enemy_stats
    else:
        pokemon_stats_dict = pokemon_stats
        
    if pokemon in pokemon_stats_dict:
        damage = random.randint(10, 50)
        pokemon_stats_dict[pokemon]["health"] -= damage
        #implemented messagebox for visual component of the game.
        messagebox.showinfo("Attack", f"{pokemon} dealt {damage} damage!")
        display_stats(pokemon, is_enemy)
#similar concept to attack funciton.enemy/player, then add health instead of subtract
def defend(pokemon, is_enemy=False):
    if is_enemy:
        pokemon_stats_dict = pokemon_enemy_stats
    else:
        pokemon_stats_dict = pokemon_stats
        
    if pokemon in pokemon_stats_dict:
        boost = random.randint(5, 30)
        pokemon_stats_dict[pokemon]["health"] += boost
        messagebox.showinfo("Defend", f"{pokemon} increased health by {boost}!")
        display_stats(pokemon, is_enemy)

def battle(pokemon):
    # pulled this from chatGPT, wasnt sure how to randomly choose items specfically from a variable.
    enemy_pokemon = random.choice(list(pokemon_enemy_stats.keys()))
    messagebox.showinfo("Battle", f"Enemy {enemy_pokemon} appears!")

    #Game logic also pulled from ChatGPT in specific lines 63 - 68
    while pokemon_stats[pokemon]["health"] > 0 and pokemon_enemy_stats[enemy_pokemon]["health"] > 0:
        action = messagebox.askquestion("Action", "Do you want to Attack?")
        if action == 'yes':
            attack(pokemon)
        else:
            defend(pokemon)

        if pokemon_enemy_stats[enemy_pokemon]["health"] > 0:
            enemy_action = random.choice(["attack", "defend"])
            if enemy_action == "attack":
                attack(enemy_pokemon, is_enemy=True)
            else:
                defend(enemy_pokemon, is_enemy=True)

def create_custom_pokemon():
    custom_window = tk.Toplevel(root)
    custom_window.title("Create Your Own Pokemon")

    # Create input fields for custom Pokemon attributes
    name_label = tk.Label(custom_window, text="Name:")
    name_label.grid(row=0, column=0)
    name_entry = tk.Entry(custom_window)
    name_entry.grid(row=0, column=1)

    type_label = tk.Label(custom_window, text="Type:")
    type_label.grid(row=1, column=0)
    type_entry = tk.Entry(custom_window)
    type_entry.grid(row=1, column=1)

    power_label = tk.Label(custom_window, text="Power:")
    power_label.grid(row=2, column=0)
    power_entry = tk.Entry(custom_window)
    power_entry.grid(row=2, column=1)

    # Function to create the custom Pokemon
    def create_pokemon():
        name = name_entry.get()
        pokemon_type = type_entry.get()
        power = power_entry.get()
        result_label.config(text=f"Created {name}, a {pokemon_type} type Pokemon with power level {power}!")
        display_stats(name)

    create_button = tk.Button(custom_window, text="Create", command=create_pokemon)
    create_button.grid(row=3, columnspan=2)

root = tk.Tk()
root.title("Welcome to The Pokemon Game")
root.geometry('500x350+200+200')

label = tk.Label(root, text="Pick your Pokemon!", fg="red", bg="yellow", width=100, height=10)
label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

def create_button(root, pokemon):
    if pokemon == "Create your own Pokemon":
        button = tk.Button(root, text=pokemon, command=create_custom_pokemon)
    else:
        button = tk.Button(root, text=pokemon, command=lambda p=pokemon: battle(p))
    button.pack()

# Only the "Create your own Pokemon" button has functionality
create_button(root, "Charmander")
create_button(root, "Bulbasaur")
create_button(root, "Squirtle")
create_button(root, "Pikachu")
create_button(root, "Create your own Pokemon")

root.mainloop()
