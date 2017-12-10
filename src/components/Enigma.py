class Enigma:
    def __init__(self, shaft, plugboard):
        """
        Requires: properly initialized, valid shaft and plugboard objects
        Ensures: a simulated Enigma machine object where for an input string
        x of all uppercase letters or uncoded symbols that yields y for a
        given state, y yields x when input starting at the same state.
        """
        self.ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.shaft = shaft
        self.plugboard = plugboard

    def encode(self, s):
        """
        Ensures: if all alphabetic characters in x are capitalized, then
        for encode(x) = y, encode(y) = x.
        """
        message = ""
        for i in s:
            if i.isalpha():
                self.shaft.advance()
                i = self.ALPHA.index(i.upper())
                i = self.plugboard.key_to_rotor(i)
                i = self.shaft.encode(i)
                i = self.plugboard.rotor_to_key(i)
                message += self.ALPHA[i]
            else:
                message += i
        return message
