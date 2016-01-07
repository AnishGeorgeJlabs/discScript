"""
Contains various functions needed by the algorithm
"""
import re

club_words = ['team', 'pair', 'club', 'wear', 'style', 'combine']
# The idea is that if a sentence is of the form ...<club_word>...with...<match-object> then we ignore the match

def has_clubbing(pre_sentence):
    """
    Accepts the pre sentence of the matched word, and checks for clubbing
    :param pre_sentence: The part of the sentence before the match
    :return:
    """
    for club_word in club_words:
        sp = re.split(club_word, pre_sentence, maxsplit=1)
        if len(sp) == 1:
            continue
        elif re.search(r"\bwith\b", sp[1]):
            return True
    return False


def has_item_value(para, item):
    """
    Check whether the para contains the given item property and that it actually belongs to the product in question
    :param para: The full description
    :param item:
    :return:
    """