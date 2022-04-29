"""The dice game Yacht"""
from typing import Counter
def digits(dice, digit):
    """Return score for digits-related category"""
    return digit * dice.count(digit)
def four_of_a_kind(dice):
    """Return score for four of a kind category"""
    elements = [x for x in set(dice) if dice.count(x) >= 4]
    return 4 * elements[0] if len(elements) > 0 else 0
YACHT = (lambda x: 50 if len(set(x)) == 1 else 0)
ONES = (lambda x: digits(x, 1))
TWOS = (lambda x: digits(x, 2))
THREES = (lambda x: digits(x, 3))
FOURS = (lambda x: digits(x, 4))
FIVES = (lambda x: digits(x, 5))
SIXES = (lambda x: digits(x, 6))
FULL_HOUSE = (lambda x: sum(x) if sorted(Counter(x).values()) == [2, 3] else 0)
FOUR_OF_A_KIND = four_of_a_kind
LITTLE_STRAIGHT = (lambda x: 30 if sorted (x) == [1, 2, 3, 4, 5] else 0)
BIG_STRAIGHT = (lambda x: 30 if sorted (x) == [2, 3, 4, 5, 6] else 0)
CHOICE = sum
def score(dice, category):
    """Return score for specific dices and category"""
    return category(dice)
