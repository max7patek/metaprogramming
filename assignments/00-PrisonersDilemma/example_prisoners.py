
from random import choice

class AlwaysConfess():

    def __init__(
        self, 
        both_confess_sentence, 
        none_confess_sentence, 
        self_confess_sentence, 
        other_confess_sentence,
    ):
        pass

    def decide(self):
        return True

    def sentence(self, years):
        pass


class AlwaysRemainSilent():

    def __init__(
        self, 
        both_confess_sentence, 
        none_confess_sentence, 
        self_confess_sentence, 
        other_confess_sentence,
    ):
        pass

    def decide(self):
        return False

    def sentence(self, years):
        pass


class RandomPrisoner():

    def __init__(
        self, 
        both_confess_sentence, 
        none_confess_sentence, 
        self_confess_sentence, 
        other_confess_sentence,
    ):
        pass

    def decide(self):
        return choice([True, False])

    def sentence(self, years):
        pass

