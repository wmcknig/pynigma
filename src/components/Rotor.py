class Rotor:
    ROTOR_LENGTH = 26

    def __init__(self, t, offset = 0):
        """
        Requires: a valid sequence of ROTOR_LENGTH, containing
        every integer from 0 to ROTOR_LENGTH - 1 inclusive.
        Ensures: this is at the given rotor state (0 by default)
        """
        self.t = t
        self.offset = offset % self.ROTOR_LENGTH

    def advance_rotor(self):
        """
        Mutates: self.offset
        Ensures: self.offset = (self.offset + 1) % ROTOR_LENGTH
        """
        self.offset = (self.offset + 1) % self.ROTOR_LENGTH

    def signal_in(self, signal):
        """
        Requires: an integer from 0 to ROTOR_LENGTH representing the
        absolute position of the signal
        Ensures: the output position of the signal, in absolute terms
        """
        #get relative signal position from input and obtain relative output
        output = self.t[(signal + self.offset) % self.ROTOR_LENGTH]
        #return absolute output signal position
        return (output - self.offset) % self.ROTOR_LENGTH

    def signal_out(self, signal):
        """
        Requires: an integer from 0 to ROTOR_LENGTH representing the
        absolute position of the signal
        Ensures: the output position of the signal, in absolute terms
        """
	#get output for relative input position, get absolute output
        output = self.t.index((signal + self.offset) % self.ROTOR_LENGTH)
        return (output - self.offset) % self.ROTOR_LENGTH
