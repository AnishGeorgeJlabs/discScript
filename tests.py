import unittest

from functions import has_clubbing, get_pre_sentence, has_item_value, split_para_into_sentences

para = "This is a cool case, we have a brown wallet. Match this with green khakis, or pair this brown wallet with yelllow shirt".lower()
split_para = split_para_into_sentences(para)

class TestClubbing(unittest.TestCase):

    def test_trivial_no_club(self):
        self.assertFalse(has_clubbing("Use this pair of ".lower()))

    def test_with_check_no_club(self):
        self.assertFalse(has_clubbing("With this slack ".lower()))

    def test_club_check(self):
        self.assertTrue(has_clubbing("You can pair it with ".lower()))

    def test_club_check_2(self):
        self.assertFalse(has_clubbing("You can club these ".lower()))

    def test_pre_sentence(self):
        self.assertEqual(
            get_pre_sentence("this is; a sentence"),
            " a sentence"
        )

    def test_pre_sentence_2(self):
        self.assertEqual(
            get_pre_sentence("this, is a multi. sentence"),
            " sentence"
        )

    def test_pre_sentence_3(self):
        self.assertEqual(get_pre_sentence("this is a no sentence"), "this is a no sentence")

    def test_pre_sentence_4(self):
        self.assertEqual(get_pre_sentence(". edge case"), " edge case")

    def test_split_para(self):
        self.assertTrue(len(split_para), 4)

    def test_item_value_base(self):
        self.assertTrue(any(has_item_value(sentence, "brown") for sentence in split_para))

    def test_item_value_bad_1(self):
        self.assertFalse(any(has_item_value(sentence, "green") for sentence in split_para))

    def test_item_value_bad_2(self):
        self.assertFalse(any(has_item_value(sentence, "yellow") for sentence in split_para))

if __name__ == '__main__':
    unittest.main()
