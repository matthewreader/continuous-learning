"""Generate random names of elves that might work in Santa's Workshop.  Give
'middle name' one third of the time"""
import sys
import random

def main():
    """Choose names at random from 2 tuples of names and print to screen.
    Choos a 'middle name' one thrid of the time"""
    print("Welcome to the Random Santa's Elf Name Generator.'\n")

    first = ('Tingle', 'Jingle', 'Dingle', 'Pepper', 'Shiny', 'Sugarplum',
             'Alabaster', 'Peppermint', 'Tinsel')
    middle = ('Cookie Slayer', 'Nog Goblin', 'Big Hands', 'Frostbite',
              'Big Spender', 'Funny-Feet')
    last = ('Evergreen', 'Winterbite', 'Snowball', 'Mistletoe', 'Sleighride',
            'Gingerbread', 'Fruitcake', 'Giftwrapper', 'Curlytoes')

    while True:
        first_name = random.choice(first)
        middle_name = random.choice(middle)
        last_name = random.choice(last)
        middle_name_chance = random.random()

        print("\n\n")
        if middle_name_chance > 0.333:
            print("{} {}".format(first_name, last_name), file=sys.stderr)
        else:
            print("{} '{}' {}".format(first_name, middle_name, last_name),
                  file=sys.stderr)
        print("\n\n")
        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")

        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()
    