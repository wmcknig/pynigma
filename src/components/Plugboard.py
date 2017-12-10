class Plugboard:
    PLUGBOARD_LENGTH = 26

    def __init__(self, mapping):
        """
        Requires: a valid sequence of PLUGBOARD_LENGTH, containing
        every integer from 0 to PLUGBOARD_LENGTH - 1 inclusive
        Ensures: a valid plugboard representation
        """
        self.mapping = mapping

    def key_to_rotor(self, i):
        """
        Requires: an integer from 0 to PLUGBOARD_LENGTH - 1
        Ensures: the output defined for the given input by this mapping
        """
        return self.mapping[i]

    def rotor_to_key(self, i):
        """
        Requires: an integer from 0 to PLUGBOARD_LENGTH - 1
        Ensures: the output defined by the inverse mapping for this
        """
        return self.mapping.index(i)
