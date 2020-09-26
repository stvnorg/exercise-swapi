#!/usr/bin/env python

import sys
import swapi

LOWER_END = 3
UPPER_END = 100

SANITY_CHECK_ERR_MSG = """
You need to replace the swapi BASE_URL
in your /path/lib/python{version}/swapi/settings.py
with value 'http://swapi.dev'
"""

exercise_list = [
    "All ships that appeared in Return of the Jedi",
    "All ships that have a hyperdrive rating >= 1.0",
    "All ships that have crews between 3 and 100"
]

def if_crews_between_3_and_100(crews):
    return crews > LOWER_END and crews < UPPER_END

def sanity_check(func):
    def wrapper():
        try:
            print("Running sanity check...")
            swapi.get_all("films")
            print("Sanity check passed!")
            func()
        except:
            print(SANITY_CHECK_ERR_MSG)
    return wrapper

@sanity_check
def exercise_one():
    print(exercise_list[0])
    for film in swapi.get_all("films").iter():
        try:
            if film.title == "Return of the Jedi":
                ships = film.get_starships()
                for ship in ships.iter():
                    print(ship.name)
                break
        except:
            pass

@sanity_check
def exercise_two():
    print(exercise_list[1])
    for ship in swapi.get_all("starships").iter():
        try:
            if float(ship.hyperdrive_rating) >= 1.0:
                print(ship.name)
        except:
            pass

@sanity_check
def exercise_three():
    print(exercise_list[2])
    for ship in swapi.get_all("starships").iter():
        try:
            if "-" in ship.crew:
                min_crews, max_crews = map(int, ship.crew.split("-"))
                if if_crews_between_3_and_100(min_crews):
                    print(ship.name)
                elif if_crews_between_3_and_100(max_crews):
                    print(ship.name)
            elif "," in ship.crew:
                crews = int("".join(ship.crew.split(",")))
                if if_crews_between_3_and_100(crews):
                    print(ship.name)
            else:
                crews = int(ship.crew)
                if if_crews_between_3_and_100(crews):
                    print(ship.name)
        except:
            pass

def exercise_swapi(args):
    if len(args) != 1:
        print("Usage: ./exercise.py <exercise_number>")
        print("./exercise.py 1 --> {}".format(exercise_list[0]))
        print("./exercise.py 2 --> {}".format(exercise_list[1]))
        print("./exercise.py 3 --> {}".format(exercise_list[2]))
        return 0

    if args[0] == "1":
        exercise_one()

    elif args[0] == "2":
        exercise_two()

    elif args[0] == "3":
        exercise_three()

    else:
        print("Invalid Option!")


if __name__ == '__main__':
    exercise_swapi(sys.argv[1:])
