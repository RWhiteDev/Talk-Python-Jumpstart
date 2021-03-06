import random
import time

from actors import Wizards, Creature, SmallAnimal, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    print('---------------------------------')
    print('        WIZARD GAME APP')
    print('---------------------------------')
    print()


def game_loop():

    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 50, True),
        Wizards('Evil Wizard', 1000)
    ]

    hero = Wizards('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a dark and foggy forest...'
              .format(active_creature.name, active_creature.level))
        print()

        cmd = input("Do you want to [a]ttack, [r]unaway, or [l]ook around? ")

        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('The wizard runs and hides to recover...')
                time.sleep(5)
                print('The wizards health has returned...')

        elif cmd == 'r':
            print('The wizard feels unsure of his chances and flees...')
        elif cmd == 'l':
            print('The wizard {} take a moment to check his surroundings and sees: '.format(hero.name))
            for c in creatures:
                print(' * A {} of level {}'. format(c.name, c.level))
        else:
            print('Ok, exiting the game... bye!')
            break

        if not creatures:
            print('Well Done. You defeated all the evils of the forest!')
            break

        print()


if __name__ == '__main__':
    main()
