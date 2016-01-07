"""
Contains various functions needed by the algorithm
"""
import re

club_words = ['team', 'pair', 'club', 'wear', 'style', 'combine', 'match']
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

def get_pre_sentence(pre_para):
    """ Deprecated
    Gets the starting part of a sentence, by traversing back until getting the end of the previous sentence
    :param pre_para: the first part of the para before the split
    :return:
    """
    for i in range(len(pre_para) - 1, -1, -1):
        if pre_para[i] in ".,;":
            return pre_para[i+1:]
    return pre_para


def has_item_value(sentence, item, check_key=False, key=""):
    """
    Check whether the sentence contains the given item property and that it actually belongs to the product in question
    use with any() for a list of description sentences
    :param sentence: The full sentence of the description
    :param item:
    :return:
    """
    sp = re.split(r"\b%s\b" % item, sentence, maxsplit=1)
    if len(sp) == 1:
        return False
    elif not has_clubbing(sp[0]):
        if check_key:
            return key in sp[0] or key in sp[1]
        else:
            return True
    else:
        return has_item_value(sp[1], item)      # Not to loose hope, we might just get another match


def split_para_into_sentences(para):
    """ Returns an array of sentences """
    return re.split(r'[.,;]', para)