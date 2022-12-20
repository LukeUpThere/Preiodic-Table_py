# Periodic Table
# This terminal application lets a user input elements from the periodic table
#   along with data associated with the element. It can then display this
#   information for a selected element, and display a specific piece of
#   information known about all elements.
from time import sleep
import os

### PRELOADED ELEMENTS ###
elements = {'H':{'full name':'Hydrogen',
                 'atomic number':'1',
                 'weight':'1.008',
                 'row':'1',
                 'column':'1'},
            'He':{'full name':'Helium',
                  'atomic number':'2',
                  'weight':'4.003',
                  'row':'1',
                  'column':'18'},
            'Ne':{'full name':'Neon',
                  'atomic number':'10',
                  'weight':'20.180',
                  'row':'2',
                  'column':'18'},
            'Ar':{'full name':'Argon',
                  'atomic number':'18',
                  'weight':'39.948',
                  'row':'3',
                  'column':'18'},
            'Kr':{'full name':'Krypton',
                  'atomic number':'36',
                  'weight':'83.798',
                  'row':'4',
                  'column':'18'},
            'Xe':{'full name':'Xenon',
                  'atomic number':'54',
                  'weight':'131.293',
                  'row':'5',
                  'column':'18'},
            'Cs':{'full name':'Cesium',
                  'atomic number':'55',
                  'weight':'132.905',
                  'row':'6',
                  'column':'1'},
            'Ba':{'full name':'Barium',
                  'atomic number':'56',
                  'weight':'137.327',
                  'row':'6',
                  'column':'2'},
            'Fr':{'full name':'Francium',
                  'atomic number':'87',
                  'weight':'223.020',
                  'row':'7',
                  'column':'1'},
            'Ra':{'full name':'Radium',
                  'atomic number':'88',
                  'weight':'226.025',
                  'row':'7',
                  'column':'2'}}

### FUNCTIONS ###
def show_header():
    os.system('cls')
    print("""
----- The Periodic Table of Elements -----
""")
def get_element():
    scene_active = True
    while scene_active:
        show_header()
        print("Enter 'q' to return to Main Menu.")
        
        # Gets user input for all data items
        atomic_symbol = input("Atomic Symbol: ")
        full_name = input("Element's full name: ")
        atomic_number = input("Atomic number: ")
        weight = input("Weight: ")
        row = input("Row: ")
        column = input("Column: ")
        if 'q' in(atomic_symbol, atomic_number, full_name, weight, row, column):
            scene_active = False
        
        # Check if the element is already in the dictionary
        element_exists = True if atomic_symbol in elements else False
        
        # Check if the given row/column space is occupied
        for symbol, data in elements.items():
            for key, value in data.items():
                if (key, value) == ('row', row):
                    same_row = True
                else:
                    same_row = False
                if (key, value) == ('column', column):
                    same_column = True
                else:
                    same_column = False
                space_occupied = True if same_column and same_row else False
                if space_occupied:
                    element_in_space = symbol
        
        # Alert user to space_occupied and element_exists conflicts
        if element_exists and space_occupied:
            print("\nThis element already exists.\n" +
                  "Would you like to update its information?")
            choice = input("[y] - yes\n[any other key] - Go back\n")
            if choice == 'y':
                # Add or update information in dictionary
                elements.update({atomic_symbol:{'full name':full_name,
                                               'atomic number':atomic_number,
                                               'weight':weight,
                                               'row':row,
                                               'column':column}})
                print("Information for '%s' has been updated." % atomic_symbol)
                sleep(1)
            else:
                print("Returning to start of 'Input Element' page.")
                sleep(1)
        elif space_occupied:
            print("\nThe row & column you have input is already filled by %s."
                                                            % element_in_space)
            print("Please first edit '%s' to change its row and column."
                                                            % element_in_space)
            sleep(2)
        elif element_exists:
            print("\nThat atomic symbol is in use elsewhere in the periodic" +
                " table.\nWould you like to update it with the data provided?")
            choice = input("[y] - yes\n[any other key] - Go back\n")
            if choice == 'y':
                # Add or update information in dictionary
                elements.update({atomic_symbol:{'full name':full_name,
                                               'atomic number':atomic_number,
                                               'weight':weight,
                                               'row':row,
                                               'column':column}})
                print("Information for '%s' has been updated." % atomic_symbol)
                sleep(1)
            else:
                print("Returning to start of 'Input Element' page.")
                sleep(1)
        elif scene_active:
            # Add or update information in dictionary
            elements.update({atomic_symbol:{'full name':full_name,
                                           'atomic number':atomic_number,
                                           'weight':weight,
                                           'row':row,
                                           'column':column}})
            print("Your element has been added.")
            sleep(1)
def see_selected_info():
    scene_active = True
    error_occured = False
    while scene_active:
        # Asks user what information they want, then displays selected info.
        show_header()
        print("What information would you like to see about every element?")
        print("""
        [1] - Full Name
        [2] - Atomic Number
        [3] - Weight
        [4] - Row
        [5] - Column
        [q] - Return to Main Menu
        """)
        choice = input("> ")
        if choice == '1':
            chosen_data = 'full name'
        elif choice == '2':
            chosen_data = 'atomic number'
        elif choice == '3':
            chosen_data = 'weight'
        elif choice == '4':
            chosen_data = 'row'
        elif choice == '5':
            chosen_data = 'column'
        elif choice == 'q':
            scene_active = False
            error_occured = True
        else:
            print("Error: invalid choice")
            sleep(1)
            error_occured = True
        
        # Display chosen info for every element
        if not error_occured:
            show_header()
            for symbol, data in elements.items():
                print("%s:" % symbol)
                for data_key, data_value in data.items():
                    if data_key == chosen_data:
                        print('%s: %s\n' % (data_key.title(), data_value))
            input("\nEnter any key to reset.\n")
def see_element_info():
    scene_active = True
    while scene_active:
        show_header()
        print("Enter an Atomic Symbol to see all info about that element.")
        choice = input("\nYou can also enter 'q' to return to Main Menu.\n")
        if choice in elements:
            show_header()
            for key, value in elements[choice].items():
                print('%s: %s' % (key.title(), value))
            input("\nEnter any key to reset.\n")
        elif choice == 'q':
            scene_active = False
        else:
            print("Sorry, that atomic symbol can't be found.")
            sleep(1)
def display_table(elements):
    scene_active = True
    while scene_active:
        show_header()

        # create a dic to represent the rows and columns of the periodic table
        table = {(r, c): '  ' for r in range(1, 10) for c in range(1, 19)}
    
        # add each element to the appropriate row and column in the table
        for symbol, element in elements.items():
            row = int(element['row'])
            column = int(element['column'])
            if len(symbol) >= 2:
                table[(row, column)] = symbol
            else:
                table[(row, column)] = symbol+' '

        # print the table to the terminal
        for row in range(1, 10):
            for column in range(1, 19):
                element = table[(row, column)]
                print(element, end=' ')
            print()
        
        # Give quit option
        choice = input("Press 'q' to return to main menu.\n")
        scene_active = False if choice == 'q' else True

### MAIN CODE ###
program_active = True
while program_active:
    show_header()
    print("""
Options:
[1] - View specific information about all elements.
[2] - View all information about a specific element.
[3] - Enter a new element or modify an existing one.
[4] - View the elements in the Periodic Table format.
[q] - Quit program.
""")
    choice = input("Please select an option.\n")
    if choice == '1':
        see_selected_info()
    elif choice == '2':
        see_element_info()
    elif choice == '3':
        get_element()
    elif choice == '4':
        display_table(elements)
    elif choice == 'q':
        program_active = False
    else:
        print("Sorry, that is not a valid option.")
        sleep(1)
