# TODO: define the 'EXPECTED_BAKE_TIME' constant
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer


# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining():
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    pass

# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here

# TODO: define the 'elapsed_time_in_minutes()'
EXPECTED_BAKE_TIME=40
PREPARATION_TIME=2
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.
    :param number_of_layers: int number of layers of lasagna used.
    :return: int total preparation time in minutes derived
    from 'PREPARATION_TIME'.
    Function that takes the number of layers in lasagna as an arguement
    and returns
    how many minutes for preparation taken based on the 'PREPARATION_TIME'.
    """
    return number_of_layers*PREPARATION_TIME
def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """Calculate the elapsed time in minutes.
    :param number_of_layers: int number of layers of lasagna used.
    :param elapsed_bake_time: int baking time already elapsed.
    :return: int time elapsed in minutes derived
    from preparation_time_in_minutes()
    function.
    Function that takes the number of layers in lasagna and elapsed time in baking
    as an arguement and returns how many minutes for preparation taken based on
    the 'PREPARATION_TIME'.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
