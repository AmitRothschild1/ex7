"""

Name : Amit Rothschild

ID : 322317637

Exercise : ex7

"""

import csv

# Global BST root

import csv



# Global BST root

ownerRoot = None



########################

# 0) Read from CSV -> HOENN_DATA

########################

def print_pokemon(pokemon):

    print(", ".join(f"{key}: {value}" for key, value in pokemon.items()))



def read_hoenn_csv(filename):

    """

    Reads 'hoenn_pokedex.csv' and returns a list of dicts:

      [ { "ID": int, "Name": str, "Type": str, "HP": int,

          "Attack": int, "Can Evolve": "TRUE"/"FALSE" },

        ... ]

    """

    data_list = []

    with open(filename, mode='r', encoding='utf-8') as f:

        reader = csv.reader(f, delimiter=',')  # Use comma as the delimiter

        first_row = True

        for row in reader:

            # It's the header row (like ID,Name,Type,HP,Attack,Can Evolve), skip it

            if first_row:

                first_row = False

                continue



            # row => [ID, Name, Type, HP, Attack, Can Evolve]

            if not row or not row[0].strip():

                break  # Empty or invalid row => stop

            d = {

                "ID": int(row[0]),

                "Name": str(row[1]),

                "Type": str(row[2]),

                "HP": int(row[3]),

                "Attack": int(row[4]),

                "Can Evolve": str(row[5]).upper()

            }

            data_list.append(d)

    return data_list





HOENN_DATA = read_hoenn_csv("hoenn_pokedex.csv")


########################
# 1) Helper Functions
########################

def read_safe_integer(prompt):
    # Safely reads an integer from user input
    while True:
        print(prompt, end="")  # Display the prompt without a new line
        user_input = input().strip()  # Read and strip extra spaces from the input

        if user_input.lstrip('-').isdigit():  # Check if the input is a valid integer (handles negative numbers)
            return int(user_input)  # Convert to integer and return
        else:
            return None  # Return None if the input is not a valid integer

def get_pokemon_by_id(pokemon_id):
    # Retrieves a Pokémon by its ID from the HOENN_DATA list
    if 0 <= pokemon_id < len(HOENN_DATA):  # Check if the ID is within valid range
        return HOENN_DATA[pokemon_id]  # Return the Pokémon dictionary
    return None  # Return None if the ID is invalid

def get_pokemon_by_name(name):
    # Searches for a Pokémon by its name (case-insensitive)
    for pokemon in HOENN_DATA:
        if pokemon["Name"].lower() == name.lower():  # Compare names in lowercase
            return pokemon  # Return the Pokémon dictionary if found
    return None  # Return None if no Pokémon with the given name is found

def display_pokemon_list(pokemon_list):
    # Displays the details of each Pokémon in the provided list
    for pokemon in pokemon_list:
        print_pokemon(pokemon)  # Call the print_pokemon function to display details

########################

# 2) BST (By Owner Name)

########################


def read_safe_integer(prompt):
    # Safely reads an integer from user input
    while True:
        print(prompt, end="")  # Display the prompt without a new line
        user_input = input().strip()  # Read and strip extra spaces from the input

        if user_input.lstrip('-').isdigit():  # Check if the input is a valid integer (handles negative numbers)
            return int(user_input)  # Convert to integer and return
        else:
            return None  # Return None if the input is not a valid integer

def get_pokemon_by_id(pokemon_id):
    # Retrieves a Pokémon by its ID from the HOENN_DATA list
    if 0 <= pokemon_id < len(HOENN_DATA):  # Check if the ID is within valid range
        return HOENN_DATA[pokemon_id]  # Return the Pokémon dictionary
    return None  # Return None if the ID is invalid

def get_pokemon_by_name(name):
    # Searches for a Pokémon by its name (case-insensitive)
    for pokemon in HOENN_DATA:
        if pokemon["Name"].lower() == name.lower():  # Compare names in lowercase
            return pokemon  # Return the Pokémon dictionary if found
    return None  # Return None if no Pokémon with the given name is found

def display_pokemon_list(pokemon_list):
    # Displays the details of each Pokémon in the provided list
    for pokemon in pokemon_list:
        print_pokemon(pokemon)  # Call the print_pokemon function to display details

def create_owner_node(owner_name, first_pokemon):
    # Creates a new BST node representing a Pokémon owner
    return {
        "owner": owner_name,        # Owner's name
        "pokedex": [first_pokemon], # List containing the first Pokémon
        "left": None,               # Left child in the BST (initially None)
        "right": None               # Right child in the BST (initially None)
    }

def new_pokedex():
    global ownerRoot  # Access the global BST root

    print("Owner name:", end=" ")
    name = input().strip()  # Read and strip the owner's name

    # Display starter Pokémon options
    print("Choose your starter Pokemon:")
    print("1) Treecko")
    print("2) Torchic")
    print("3) Mudkip")

    choice = read_safe_integer("Your choice: ")  # Get the user's choice

    # Select the corresponding starter Pokémon
    if choice == 1:
        first_pokemon = get_pokemon_by_name("Treecko")
    elif choice == 2:
        first_pokemon = get_pokemon_by_name("Torchic")
    elif choice == 3:
        first_pokemon = get_pokemon_by_name("Mudkip")
    else:
        print("Invalid. No new Pokedex created.")  # Handle invalid choice
        return

    # Create a new owner node and insert it into the BST
    new_owner = create_owner_node(name, first_pokemon)
    ownerRoot = insert_owner_bst(ownerRoot, new_owner)

    print(f"New Pokedex created for {name} with starter {first_pokemon['Name']}.")

###############################################################################################
def insert_owner_bst(root, new_owner_node):
    # If the tree is empty, return the new owner as the root
    if root is None:
        return new_owner_node

    # Compare owner names for alphabetical sorting
    if new_owner_node["owner"].lower() < root["owner"].lower():
        root["left"] = insert_owner_bst(root.get("left"), new_owner_node)  # Insert into the left subtree

    elif new_owner_node["owner"].lower() > root["owner"].lower():
        root["right"] = insert_owner_bst(root.get("right"), new_owner_node)  # Insert into the right subtree

    else:
        # The owner already exists in the tree
        print(f"Owner '{new_owner_node['owner']}' already exists in the BST.")

    return root  # Return the updated root


def find_owner_bst(root, owner_name):
    # Search for an owner by name
    if root is None:
        return None  # If we reach a leaf and haven't found the owner

    owner_name_lower = owner_name.lower()
    root_owner_lower = root["owner"].lower()

    if owner_name_lower < root_owner_lower:
        return find_owner_bst(root.get("left"), owner_name)  # Search in the left subtree

    elif owner_name_lower > root_owner_lower:
        return find_owner_bst(root.get("right"), owner_name)  # Search in the right subtree

    else:
        return root  # Owner found


def find_min_owner_node(root):
    # Find the owner with the minimum value in the subtree
    if root is None:
        return None

    while root.get("left") is not None:
        root = root["left"]  # Move left until the leftmost leaf is reached

    return root  # Return the owner with the minimum value


####################################################################################

def delete_owner_bst(root, owner_name):
    global ownerRoot  # Use of a global variable (not recommended unless necessary)
    if root is None:
        print(f"Owner '{owner_name}' not found.")
        return None  # Owner not found for deletion

    if owner_name.lower() < root["owner"].lower():
        root["left"] = delete_owner_bst(root.get("left"), owner_name)  # Delete in the left subtree

    elif owner_name.lower() > root["owner"].lower():
        root["right"] = delete_owner_bst(root.get("right"), owner_name)  # Delete in the right subtree

    else:
        # Owner found for deletion
        print(f"Deleting {owner_name}'s Pokedex...")

        # Case 1: No children (leaf node)
        if root.get("left") is None and root.get("right") is None:
            print("Pokedex deleted.")
            return None  # Delete the leaf

        # Case 2: Only one child (left or right)
        if root.get("left") is None:
            return root["right"]  # Replace current node with the right subtree

        if root.get("right") is None:
            return root["left"]  # Replace current node with the left subtree

        # Case 3: Two children - find the minimum successor in the right subtree
        successor = find_min_owner_node(root["right"])
        root["owner"] = successor["owner"]  # Copy the owner's name from the successor
        root["pokedex"] = successor["pokedex"]  # Copy additional information from the successor

        # Delete the successor node that was moved up
        root["right"] = delete_owner_bst(root["right"], successor["owner"])

    return root  # Return the updated root


def find_min_owner_node(root):
    # Find the node with the minimum value (reusable function)
    current = root
    while current.get("left") is not None:
        current = current["left"]  # Move left until the leftmost node
    return current

########################

# 3) BST Traversals

########################
def bfs_traversal(root):
    # Breadth-First Search (BFS) traversal starting from the root node
    if root is None:
        return

    queue = [root]  # Initialize the queue with the root node

    while queue:
        current = queue.pop(0)  # Dequeue the first node in the queue
        print(f"Owner: {current['owner']}")  # Print the owner's name
        display_pokemon_list(current.get("pokedex", []))  # Display the Pokémon list
        print()

        # Enqueue the left child if it exists
        if current.get("left") is not None:
            queue.append(current["left"])

        # Enqueue the right child if it exists
        if current.get("right") is not None:
            queue.append(current["right"])


def pre_order_traversal(root):
    """ Pre-order traversal (root -> left -> right) """
    if root is None:
        return

    print(f"Owner: {root['owner']}")  # Print the owner's name
    display_pokemon_list(root.get("pokedex", []))  # Display the Pokémon list
    print()

    # Recursively traverse the left subtree
    pre_order_traversal(root.get("left"))
    # Recursively traverse the right subtree
    pre_order_traversal(root.get("right"))


def in_order_traversal(root):
    """ In-order traversal (left -> root -> right) """
    if root is None:
        return

    # Recursively traverse the left subtree
    in_order_traversal(root.get("left"))

    print(f"Owner: {root['owner']}")  # Print the owner's name
    display_pokemon_list(root.get("pokedex", []))  # Display the Pokémon list
    print()

    # Recursively traverse the right subtree
    in_order_traversal(root.get("right"))


def post_order_traversal(root):
    """ Post-order traversal (left -> right -> root) """
    if root is None:
        return

    # Recursively traverse the left subtree
    post_order_traversal(root.get("left"))
    # Recursively traverse the right subtree
    post_order_traversal(root.get("right"))

    print(f"Owner: {root['owner']}")  # Print the owner's name
    display_pokemon_list(root.get("pokedex", []))  # Display the Pokémon list
    print()

########################

# 4) Pokedex Operations

########################

def add_pokemon_to_owner(owner_node):
    # Prompt the user to enter a Pokémon ID
    poke_id = read_safe_integer("Enter Pokémon ID to add: ")

    # Validate the Pokémon ID
    if poke_id is None or poke_id <= 0 or poke_id > 135:
        print(f"ID {poke_id} not found in Hoenn data.")
        return

    # Check if the Pokémon already exists in the owner's Pokedex
    for pokemon in owner_node["pokedex"]:
        if pokemon["ID"] == poke_id:
            print("Pokémon already in the Pokedex. No changes made.")
            return

    # Retrieve the Pokémon data using its ID and add it to the owner's Pokedex
    new_pokemon = get_pokemon_by_id(poke_id - 1)
    if new_pokemon:
        owner_node["pokedex"].append(new_pokemon)
        print(f"Pokémon {new_pokemon['Name']} (ID {poke_id}) added to {owner_node['owner']}'s Pokedex.")
    else:
        print(f"Pokémon with ID {poke_id} not found.")


def release_pokemon_by_name(owner_node):
    """Remove a Pokémon from the owner's Pokedex by name."""
    # Prompt the user to enter the Pokémon's name
    name = input("Enter Pokémon name to release: ").strip()

    # Search for the Pokémon in the owner's Pokedex
    pokemon_to_remove = None
    for pokemon in owner_node["pokedex"]:
        if pokemon["Name"].lower() == name.lower():
            pokemon_to_remove = pokemon
            break

    # Remove the Pokémon if found
    if pokemon_to_remove:
        owner_node["pokedex"].remove(pokemon_to_remove)
        print(f"Releasing {pokemon_to_remove['Name']} from {owner_node['owner']}'s Pokedex.")
    else:
        print(f"No Pokémon named '{name}' in {owner_node['owner']}'s Pokedex.")


def evolve_pokemon_by_name(owner_node):
    """Evolve a Pokémon by name if possible, handling duplicates if needed."""
    # Prompt the user to enter the Pokémon's name
    name = input("Enter Pokémon name to evolve: ").strip()

    # Find the Pokémon in the owner's Pokedex
    pokemon_to_evolve = None
    for pokemon in owner_node["pokedex"]:
        if pokemon["Name"].lower() == name.lower():
            pokemon_to_evolve = pokemon
            break

    # Handle the case where the Pokémon is found
    if pokemon_to_evolve:
        if pokemon_to_evolve["CanEvolve"] == "TRUE":
            # Get the evolved form of the Pokémon
            evolved_pokemon = get_pokemon_by_id(pokemon_to_evolve["ID"])

            # Check if the evolved form is already present in the Pokedex
            already_present = any(p["ID"] == evolved_pokemon["ID"] for p in owner_node["pokedex"])

            # Remove the current Pokémon
            owner_node["pokedex"].remove(pokemon_to_evolve)

            if already_present:
                print(
                    f"Pokémon evolved from {pokemon_to_evolve['Name']} (ID {pokemon_to_evolve['ID']}) "
                    f"to {evolved_pokemon['Name']} (ID {evolved_pokemon['ID']})."
                )
                print(f"{evolved_pokemon['Name']} was already present; releasing it immediately.")
            else:
                # Add the evolved Pokémon if it's not already present
                owner_node["pokedex"].append(evolved_pokemon)
                print(
                    f"Pokémon evolved from {pokemon_to_evolve['Name']} (ID {pokemon_to_evolve['ID']}) "
                    f"to {evolved_pokemon['Name']} (ID {evolved_pokemon['ID']})."
                )
        else:
            print(f"{pokemon_to_evolve['Name']} cannot evolve.")
    else:
        print(f"No Pokémon named '{name}' in {owner_node['owner']}'s Pokedex.")

########################

# 5) Sorting Owners by # of Pokemon

########################
def gather_all_owners(root, owner_list):
    """
    Collect all BST nodes (owners) into a list using in-order traversal.
    """
    if root is None:
        return

    # Traverse the left subtree
    gather_all_owners(root.get("left"), owner_list)

    # Add the current owner to the list
    owner_list.append(root)

    # Traverse the right subtree
    gather_all_owners(root.get("right"), owner_list)


def sort_owners_by_num_pokemon():
    # Gather all owners from the BST
    owner_list = []
    gather_all_owners(ownerRoot, owner_list)

    if not owner_list:
        print("No owners available.")
        return

    print("=== Owners Sorted by Number of Pokémon ===")

    # Sort owners by the number of Pokémon, then alphabetically by owner name if equal
    sorted_owners = sorted(owner_list, key=lambda owner: (len(owner.get("pokedex", [])), owner["owner"].lower()))

    # Display the sorted owners
    for owner in sorted_owners:
        print(f"Owner: {owner['owner']} (has {len(owner.get('pokedex', []))} Pokémon)")
        print()

########################

# 6) Print All

########################

def print_all_owners():
    # Menu for selecting traversal method
    print("=== Choose Traversal Method ===")
    print("1) Breadth-First Search (BFS)")
    print("2) Pre-Order Traversal")
    print("3) In-Order Traversal")
    print("4) Post-Order Traversal")

    # Read the user's choice
    option = read_safe_integer("Your choice: ")
    print()

    # Perform the selected traversal
    if option == 1:
        bfs_traversal(ownerRoot)
    elif option == 2:
        pre_order_traversal(ownerRoot)
    elif option == 3:
        in_order_traversal(ownerRoot)
    elif option == 4:
        post_order_traversal(ownerRoot)
    else:
        print("Invalid choice. Please select a number between 1 and 4.")

########################

# 7) The Display Filter Sub-Menu

########################

def display_filter_sub_menu(owner_node):
    """
    Display a sub-menu to filter and display Pokémon based on user-selected criteria.
    """

    while True:
        # Display the filter menu
        print("""
        -- Display Filter Menu --
        1. Only a certain Type
        2. Only Evolvable
        3. Only Attack above __
        4. Only HP above __
        5. Only names starting with letter(s)
        6. All of them!
        7. Back
        """)

        # Prompt user for their choice
        choice = read_safe_integer("Your choice: ")

        if choice == 1:
            # Filter Pokémon by Type
            poke_type = input("Which Type? (e.g. GRASS, WATER): ").strip().lower()
            filtered = [p for p in owner_node["pokedex"] if p["Type"].lower() == poke_type]

        elif choice == 2:
            # Filter Pokémon that can evolve
            filtered = [p for p in owner_node["pokedex"] if p["CanEvolve"] == "TRUE"]

        elif choice == 3:
            # Filter Pokémon with Attack above a threshold
            threshold = read_safe_integer("Enter Attack threshold: ")
            while threshold is None:
                print("Invalid input.")
                threshold = read_safe_integer("Enter Attack threshold: ")

            filtered = [p for p in owner_node["pokedex"] if p["Attack"] > threshold]

        elif choice == 4:
            # Filter Pokémon with HP above a threshold
            threshold = read_safe_integer("Enter HP threshold: ")
            while threshold is None:
                print("Invalid input.")
                threshold = read_safe_integer("Enter HP threshold: ")

            filtered = [p for p in owner_node["pokedex"] if p["HP"] > threshold]

        elif choice == 5:
            # Filter Pokémon with names starting with specific letters
            prefix = input("Starting letter(s): ").strip().lower()
            filtered = [p for p in owner_node["pokedex"] if p["Name"].lower().startswith(prefix)]

        elif choice == 6:
            # Display all Pokémon in the Pokedex
            filtered = owner_node["pokedex"]

        elif choice == 7:
            # Exit the sub-menu
            print("Back to Pokedex Menu.")
            break

        else:
            print("Invalid choice.")
            continue

        # Display filtered Pokémon or a message if none match
        if not filtered:
            print("There are no Pokémons in this Pokedex that match the criteria.")
        else:
            display_pokemon_list(filtered)


########################

# 8) Sub-menu & Main menu

########################
def existing_pokedex():
    """
    Ask the user for an owner name, locate the BST node, then show a sub-menu:
    - Add Pokémon
    - Display (Filter)
    - Release
    - Evolve
    - Back
    """

    print("Owner name: ", end="")
    name = input().strip().lower()  # Get the owner's name from the user

    if ownerRoot is None:
        print("No owners at all.")  # Handle the case where no owners exist
        return

    owner = find_owner_bst(ownerRoot, name)  # Find the owner in the BST

    if owner is None:
        print(f"Owner '{name}' not found.")  # Handle the case where the owner is not found
        return

    print("")

    # Display the Pokedex sub-menu for the specific owner
    while True:
        print(f"-- {name}'s Pokedex Menu --")
        print("1. Add Pokémon")
        print("2. Display Pokedex")
        print("3. Release Pokémon")
        print("4. Evolve Pokémon")
        print("5. Back to Main")

        choice = read_safe_integer("Your choice: ")  # Get the user's choice

        while choice is None:
            print("Invalid input.")
            choice = read_safe_integer("Your choice: ")

        # Perform the corresponding action based on the user's choice
        if choice == 1:
            add_pokemon_to_owner(owner)  # Add a Pokémon to the owner's Pokedex

        elif choice == 2:
            display_filter_sub_menu(owner)  # Display the Pokémon with filter options

        elif choice == 3:
            release_pokemon_by_name(owner)  # Release a Pokémon from the owner's Pokedex

        elif choice == 4:
            evolve_pokemon_by_name(owner)  # Evolve a Pokémon if possible

        elif choice == 5:
            print("Back to Main Menu.")  # Return to the main menu
            break

        else:
            print("Invalid choice.")  # Handle invalid input


def main_menu():
    """
    Main menu for:
    1) New Pokedex
    2) Existing Pokedex
    3) Delete a Pokedex
    4) Sort owners
    5) Print all
    6) Exit
    """

    while True:
        print("\n=== Main Menu ===")
        print("1. New Pokedex")
        print("2. Existing Pokedex")
        print("3. Delete a Pokedex")
        print("4. Display owners by number of Pokémon")
        print("5. Print All")
        print("6. Exit")

        choice = read_safe_integer("Your choice: ")  # Get the user's choice

        # Perform the corresponding action based on the user's choice
        if choice == 1:
            new_pokedex()  # Create a new Pokedex

        elif choice == 2:
            existing_pokedex()  # Manage an existing Pokedex

        elif choice == 3:
            global ownerRoot  # Access the global ownerRoot variable

            print("Enter owner to delete: ", end="")
            name = input().strip()  # Get the owner's name to delete

            owner = find_owner_bst(ownerRoot, name)  # Find the owner in the BST
            ownerRoot = delete_owner_bst(ownerRoot, name)  # Delete the owner from the BST

        elif choice == 4:
            sort_owners_by_num_pokemon()  # Display owners sorted by the number of Pokémon

        elif choice == 5:
            print_all_owners()  # Print all owners with their Pokedex information

        elif choice == 6:
            print("Goodbye!")  # Exit the program
            break

        else:
            print("Invalid choice.")  # Handle invalid input



def main():
    main_menu()


if __name__ == "__main__":
    main()
