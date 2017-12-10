class Shaft:
    def __init__(self, rotors, notches, reflector):
        """
        Requires: a sequence of rotor objects starting from the most-frequently
        turned one, a  of notches (represented as integers from 0
        to ROTOR_LENGTH - 1) for each respective rotor minus the last one,
        and a single reflector object
        Ensures: a set of rotors in their starting positions
        """
        self.rotors = rotors
        self.notches = notches
        self.reflector = reflector

    def advance(self):
        """
        Ensures: the first rotor is advanced one step, every rotor is
        advanced at most one step, and every rotor at its respective
        notch position is advanced alongside its immediate "higher"
        neighbor
        """
        to_advance = [False for i in self.rotors]
        #first rotor guaranteed to be advanced
        to_advance[0] = True
        #toggle rotor advances by notch engagements
        for i in range(len(self.notches)):
            if self.rotors[i].offset == self.notches[i]:
                to_advance[i] = True
                to_advance[i + 1] = True
        #advance every rotor to be advanced
        for i in range(len(to_advance)):
            if to_advance[i]:
                self.rotors[i].advance_rotor()

    def encode(self, signal):
        """
        Requires: an integer from 0 to ROTOR_LENGTH - 1
        Ensures: for the same object state, i == encode(encode(i))
        """
        #signal in route
        for i in self.rotors:
            signal = i.signal_in(signal)
        #through reflector
        signal = self.reflector.reflect(signal)
        #signal out route
        for i in self.rotors[::-1]:
            signal = i.signal_out(signal)
        return signal
