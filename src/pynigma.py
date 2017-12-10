from sys import argv
from components.Enigma import *
from components.Rotor import *
from components.Reflector import *
from components.Shaft import *
from components.Plugboard import *

def buildenigma(fn):
    """
    Builds an Enigma object from the given file object.
    Returns the Enigma object.
    """
    plugboard = [i for i in range(Plugboard.PLUGBOARD_LENGTH)]
    rotors = []
    notches = []
    reflector = []
    offsets = []

    for i in fn:
        i = i.strip().split()
        if i[0] == "ROTOR":
            rotors.append([int(j) for j in i[2:]])
            offsets.append(0)
        elif i[0] == "PLUGBOARD":
            pb = [int(j) for j in i[2:]]
        elif i[0] == "NOTCHES":
            notches = [int(j) for j in i[2:]]
        elif i[0] == "REFLECTOR":
            reflector = [int(j) for j in i[2:]]
        elif i[0] == "OFFSETS":
            offsets = [int(j) for j in i[2:]]

    PLUGBOARD = Plugboard(plugboard)
    ROTORS = [Rotor(i[0], i[1]) for i in zip(rotors, offsets)]
    REFLECTOR = Reflector(reflector)
    SHAFT = Shaft(ROTORS, notches, REFLECTOR)
    return Enigma(SHAFT, PLUGBOARD)

if __name__ == "__main__":
    if len(argv) < 4:
        print("Use program as pynigma CONFIG INPUT OUTPUT")
        exit()

    config = open(argv[1], 'r')
    e = buildenigma(config)
    config.close()

    f = open(argv[2], 'r')
    g = open(argv[3], 'w')
    for i in f:
        g.write(e.encode(i))
    f.close()
    g.close()
