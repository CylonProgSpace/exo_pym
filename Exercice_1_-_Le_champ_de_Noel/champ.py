# Met ton code ici


###########################
####### 1: Un champ #######
###########################

from random import random, randint


def generate_tree(disponible_place: int, number_line, number_tree_line: int = 25):
    number_tree_left = number_tree_line
    my_field = [None] * disponible_place
    while number_tree_left != 0 or None in my_field:
        place_tree = round(random())
        if None not in my_field:

            all_available_space = []
            for counter, character in enumerate(my_field):
                if character == " ":
                    all_available_space.append(counter)

            place_to_tree = all_available_space[
                randint(0, len(all_available_space) - 1)
            ]

            my_field[place_to_tree] = "0"

            number_tree_left -= 1
        else:
            place = randint(0, len(my_field) - 1)
            while my_field[place] != None:
                place = randint(0, len(my_field) - 1)
            if place_tree and number_tree_left != 0:
                my_field[place] = "0"
                number_tree_left -= 1
            else:
                my_field[place] = " "

    my_field = "".join(my_field)
    print(my_field, end="")


def rectangle(height: int = 100, width: int = 10):
    print("#" * height)
    for number_line in range(width):
        print("#", end="")

        number_tree = generate_tree(height - 2, number_line)
        print("#")
    print("#" * height)


rectangle()
