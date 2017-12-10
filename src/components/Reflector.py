class Reflector:
    REFLECTOR_LENGTH = 26

    def __init__(self, t):
        """
        Requires: a valid tuple of length REFLECTOR_LENGTH, 
        containing every integer from 0 to REFLECTOR_LENGTH
	inclusive, where for every element t[position] != position
        and if t[x] = y then t[y] = x
        Ensures: this is a valid reflector, where if an input signal s
        yields t, input signal t yields s
        """
        self.t = t

    def reflect(self, signal):
        return self.t[signal]
